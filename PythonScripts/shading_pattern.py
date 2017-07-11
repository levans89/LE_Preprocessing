# -*- coding: utf-8 -*-
"""
Script for background subtraction, instead of rolling ball
"""
from pyAnalyzer import illum_correction
setting_file = "W:/2015_09_HTS_LE/Code_LE/Global_config/basicSettingsLocal.py"
redo = False

corrector = illum_correction.IllumCorrection(setting_file, redo=redo)

# step 1, compute shading pattern
# sigma=100 for plates with cells, 50 without (to be verified)

# TEST VALUES FROM ALICE, just to test it's working
plateList = ['LE_20170628_InCell2000_plate_2017018376_10x_t48',
             'LE_20170628_InCell2000_plate_2017018372_10x_t48',
             'LE_20170628_InCell2000_plate_2017018371_10x_t48',
             'LE_20170628_InCell2000_plate_2017018370_10x_t48',
             'LE_20170628_InCell2000_plate_2017018369_10x_t48',
             'LE_20170628_InCell2000_plate_2017018368_10x_t48',
             'LE_20170628_InCell2000_plate_2017018367_10x_t48',
             'LE_20170628_InCell2000_plate_2017018366_10x_t48',
             'LE_20170628_InCell2000_plate_2017018365_10x_t48',
             'LE_20170628_InCell2000_plate_2017018364_10x_t48',
             'LE_20170628_InCell2000_plate_2017018363_10x_t48',
             'LE_20170628_InCell2000_plate_2017018362_10x_t48',
             'LE_20170628_InCell2000_plate_2017018361_10x_t48',
             'LE_20170628_InCell2000_plate_2017018360_10x_t48',
             'LE_20170628_InCell2000_plate_2017018359_10x_t48',
             'LE_20170628_InCell2000_plate_2017018358_10x_t48',
             'LE_20170628_InCell2000_plate_2017018357_10x_t48',
             'LE_20170628_InCell2000_plate_2017018356_10x_t48',
             'LE_20170628_InCell2000_plate_2017018355_10x_t48',
             'LE_20170628_InCell2000_plate_2017018354_10x_t48',
             'LE_20170628_InCell2000_plate_2017018352_10x_t48',
             'LE_20170628_InCell2000_plate_2017018351_10x_t48',
             'LE_20170628_InCell2000_plate_2017018350_10x_t48',
             'LE_20170628_InCell2000_plate_2017018349_10x_t48',
             'LE_20170628_InCell2000_plate_2017018348_10x_t48',
             'LE_20170628_InCell2000_plate_2017018347_10x_t48',
             'LE_20170628_InCell2000_plate_2017018346_10x_t48',
             'LE_20170628_InCell2000_plate_2017018345_10x_t48',
             'LE_20170628_InCell2000_plate_2017018344_10x_t48',
             'LE_20170628_InCell2000_plate_2017018343_10x_t48',
             'LE_20170628_InCell2000_plate_2017018342_10x_t48',
             'LE_20170628_InCell2000_plate_2017018341_10x_t48',
             'LE_20170628_InCell2000_plate_2017018340_10x_t48',
             'LE_20170628_InCell2000_plate_2017018339_10x_t48',
             'LE_20170628_InCell2000_plate_2017018338_10x_t48',
             'LE_20170628_InCell2000_plate_2017018337_10x_t48',
             'LE_20170628_InCell2000_plate_2017018336_10x_t48']
sigma = 50

corrector.compute_illumination_mask(plateList, sigma)


# To compute the image of the shading pattern
filename = corrector.settings.illum_file.format(plateList[0], sigma)
corrector.plot(filename)