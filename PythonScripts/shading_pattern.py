# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 09:38:38 2017

@author: LEEvans

Script for background subtraction, instead of rolling ball
"""

setting_file = "W:/2015_09_HTS_LE/code/Global_config/basicSettings.py"
redo = False

from pyAnalyzer import illum_correction
corrector = illum_correction.IllumCorrection(setting_file, redo=redo)

#step 1, compute shading pattern
#sigma=100 for plates with cells, 50 without (to be verified)

    #TEST VALUES FROM ALICE, just to test it's working
plateList = ['LE_20170211_nikon210X_plate_2017018130_t48']
sigma = 50

corrector.compute_illumination_mask(plateList,sigma)


## To compute the image of the shading pattern
filename = corrector.illum_file.format(plateList[0], sig_seq = [50, 75, 100])
corrector.plot(filename)