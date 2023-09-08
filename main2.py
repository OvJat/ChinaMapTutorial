#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Support Python 3.10
    @author: Lou Xiao(louxiao@i32n.com)
    @maintainer: Lou Xiao(louxiao@i32n.com)
    @copyright: Copyright 2018~2023
    @created time: 2023-09-08 23:44:34 CST
    @updated time: 2023-09-08 23:44:34 CST
"""

import os.path
import numpy as np
import cartopy.crs as ccrs
from cartopy.io import shapereader
from matplotlib import pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    image_file = "china_map_style2.png"
    china_shp_file = os.path.join(SCRIPT_DIR, 'data', 'ChinaMap', "china.shp")

    plt.figure(figsize=(7, 6), dpi=300)
    # cylindrical projections
    proj = ccrs.PlateCarree()
    # init axes
    ax = plt.axes(projection=proj)

    # title
    ax.set_title("China Map @2022 Style 2")

    # set region: West:70˚, East:140˚, North:60˚, South:15˚
    ax.set_extent([70, 140, 60, 15], crs=proj)
    ax.set_xticks(np.linspace(70, 140, 15))
    ax.set_yticks(np.linspace(60, 15, 10))

    # draw china mainland map
    shp = shapereader.Reader(china_shp_file).geometries()
    ax.add_geometries(shp, crs=proj, facecolor='none', edgecolor='red', lw=0.5)
    # ax.gridlines(crs=proj, draw_labels=False, linewidth=1, color='gray', alpha=0.5, linestyle='--')

    # draw south map
    ax_sub = plt.axes([0, 0, 10 / 70, 12 / 70], projection=proj)
    ax_sub.set_extent([105, 125, 24, 0], crs=proj)
    shp = shapereader.Reader(china_shp_file).geometries()
    ax_sub.add_geometries(shp, crs=proj, facecolor='none', edgecolor='red', lw=0.5)
    p1 = ax.get_position()
    p2 = ax_sub.get_position()
    ax_sub.set_position([p1.x0 + p1.width - p2.width, p1.y0, p2.width, p2.height])

    # uncomment below lines to draw Natural Earth shaded relief
    # os.environ['CARTOPY_USER_BACKGROUNDS'] = os.path.join(SCRIPT_DIR, 'data', 'NaturalEarth')
    # ax.background_img(name='ne_shaded', resolution='full')
    # ax_sub.background_img(name='ne_shaded', resolution='full')

    # save image file
    plt.savefig(image_file, bbox_inches='tight')


if __name__ == '__main__':
    main()
