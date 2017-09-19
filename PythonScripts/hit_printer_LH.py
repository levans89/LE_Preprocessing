# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:59:24 2017
@author: LEEvans
"""
import csv
import sys
sys.path.insert(0, 'W:\PyCommonLibrary\pysrc')
from pyExplorer.rawDataExplorer import imageprint

printer = imageprint.ImagePrinter('W:\\2015_09_HTS_LE\\Code_LE\Global_config\\basicSettingsLocal.py')
levelsets = [(40, 800), (40, 800), (40, 800), (40, 800)]  # between 0 and 4095 for 2x2 binned image
color_order = ["B", "G", "R", "W"]  # Tell colors for channels in the same order.
# Only options: R for red, G for green, B for blue and W for white
crop = 1024
output_folder = 'W:\\2015_09_HTS_LE\\results\\Images\\Bigscreen_432'
hitlist_file = "W:\\2015_09_HTS_LE\\results\\matlab_results\\bigscreen\\hitlist_p10-3.csv"


def le_printer(hitlist_file):
    hitlist = []
    with open(hitlist_file, newline = '') as csvfile:
        hitlist_i = csv.reader(csvfile)
        for row in hitlist_i:
            hitlist.append(row)
            
    for p in range(len(hitlist)):
        plateNames=hitlist[p][2]
        print(plateNames)
        wells = hitlist[p][1]
        print(wells)
        try:
            printer.image_print(plateList=hitlist[p][2], wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",crop=crop, output_folder=output_folder)
        except:
            pass

le_printer(hitlist_file)

