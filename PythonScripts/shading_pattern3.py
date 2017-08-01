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

plateList = ['LE_20170719_InCell2000_plate_2017018399_10x_t48',
             'LE_20170719_InCell2000_plate_2017018398_10x_t48',
             'LE_20170719_InCell2000_plate_2017018397_10x_t48',
             'LE_20170719_InCell2000_plate_2017018396_10x_t48',
             'LE_20170719_InCell2000_plate_2017018395_10x_t48',
             'LE_20170719_InCell2000_plate_2017018394_10x_t48',
             'LE_20170719_InCell2000_plate_2017018393_10x_t48',
             'LE_20170719_InCell2000_plate_2017018392_10x_t48',
             'LE_20170719_InCell2000_plate_2017018391_10x_t48',
             'LE_20170719_InCell2000_plate_2017018390_10x_t48',
             'LE_20170719_InCell2000_plate_2017018389_10x_t48',
             'LE_20170719_InCell2000_plate_2017018388_10x_t48',
             'LE_20170719_InCell2000_plate_2017018387_10x_t48',
             'LE_20170719_InCell2000_plate_2017018386_10x_t48',
             'LE_20170719_InCell2000_plate_2017018385_10x_t48',
             'LE_20170719_InCell2000_plate_2017018384_10x_t48',
             'LE_20170719_InCell2000_plate_2017018383_10x_t48',
             'LE_20170719_InCell2000_plate_2017018382_10x_t48',
             'LE_20170719_InCell2000_plate_2017018381_10x_t48',
             'LE_20170719_InCell2000_plate_2017018380_10x_t48',
             'LE_20170719_InCell2000_plate_2017018379_10x_t48',
             'LE_20170719_InCell2000_plate_2017018378_10x_t48',
             'LE_20170719_InCell2000_plate_2017018377_10x_t48']
sigma = 50

corrector.compute_illumination_mask(plateList, sigma)


# To compute the image of the shading pattern
filename = corrector.settings.illum_file.format(plateList[0], sigma)
corrector.plot(filename)