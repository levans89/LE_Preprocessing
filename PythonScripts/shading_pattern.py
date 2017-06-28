# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 09:38:38 2017

@author: LEEvans

Script for background subtraction, instead of rolling ball
"""
from pyAnalyzer import illum_correction
setting_file = "W:/2015_09_HTS_LE/Code_LE/Global_config/basicSettingsLocal.py"
redo = False

corrector = illum_correction.IllumCorrection(setting_file, redo=redo)

# step 1, compute shading pattern
# sigma=100 for plates with cells, 50 without (to be verified)

# TEST VALUES FROM ALICE, just to test it's working
plateList = ['LE_20170515_InCell2000_plate_2017018235_10x_t48']
sigma = 100

corrector.compute_illumination_mask(plateList, sigma)


# To compute the image of the shading pattern
filename = corrector.settings.illum_file.format(plateList[0], 100)
corrector.plot(filename)