#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Support Python 3.10
    @author: Lou Xiao(louxiao@i32n.com)
    @maintainer: Lou Xiao(louxiao@i32n.com)
    @copyright: Copyright 2018~2023
    @created time: 2023-09-08 12:12:47 CST
    @updated time: 2023-09-08 12:12:47 CST
"""

import os.path
import numpy as np
import cartopy.crs as ccrs
from cartopy.io import shapereader
from matplotlib import pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    image_file = "china_map.png"
    china_shp_file = os.path.join(SCRIPT_DIR, 'data', 'ChinaMap', "china.shp")

    plt.figure(figsize=(7, 6), dpi=300)
    # cylindrical projections
    proj = ccrs.PlateCarree()
    # init axes
    ax = plt.axes(projection=proj)

    # title
    ax.set_title("China Map")

    # set region: West:70˚, East:140˚, North:60˚, South:0˚
    ax.set_extent([70, 140, 60, 0], crs=proj)
    ax.set_xticks(np.linspace(70, 140, 15))
    ax.set_yticks(np.linspace(60, 0, 13))

    # uncomment below two lines to draw Natural Earth shaded relief
    # os.environ['CARTOPY_USER_BACKGROUNDS'] = os.path.join(SCRIPT_DIR, 'data', 'NaturalEarth')
    # ax.background_img(name='ne_shaded', resolution='full')

    # draw china map
    shp = shapereader.Reader(china_shp_file).geometries()
    ax.add_geometries(shp, crs=proj, facecolor='none', edgecolor='red', lw=0.5)

    # save image file
    plt.savefig(image_file, bbox_inches='tight')


if __name__ == '__main__':
    main()
