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
plateList = ['LE_20170627_InCell2000_plate_2017018333_10x_t48',
             'LE_20170627_InCell2000_plate_2017018332_10x_t48',
             'LE_20170627_InCell2000_plate_2017018331_10x_t48',
             'LE_20170627_InCell2000_plate_2017018330_10x_t48',
             'LE_20170627_InCell2000_plate_2017018329_10x_t48',
             'LE_20170627_InCell2000_plate_2017018328_10x_t48',
             'LE_20170627_InCell2000_plate_2017018327_10x_t48',
             'LE_20170627_InCell2000_plate_2017018326_10x_t48',
             'LE_20170627_InCell2000_plate_2017018325_10x_t48',
             'LE_20170627_InCell2000_plate_2017018324_10x_t48',
             'LE_20170627_InCell2000_plate_2017018323_10x_t48',
             'LE_20170627_InCell2000_plate_2017018322_10x_t48',
             'LE_20170627_InCell2000_plate_2017018321_10x_t48',
             'LE_20170627_InCell2000_plate_2017018320_10x_t48',
             'LE_20170627_InCell2000_plate_2017018319_10x_t48',
             'LE_20170627_InCell2000_plate_2017018318_10x_t48',
             'LE_20170627_InCell2000_plate_2017018317_10x_t48',
             'LE_20170627_InCell2000_plate_2017018316_10x_t48',
             'LE_20170627_InCell2000_plate_2017018315_10x_t48',
             'LE_20170627_InCell2000_plate_2017018314_10x_t48',
             'LE_20170627_InCell2000_plate_2017018313_10x_t48',
             'LE_20170627_InCell2000_plate_2017018312_10x_t48',
             'LE_20170627_InCell2000_plate_2017018311_10x_t48',
             'LE_20170627_InCell2000_plate_2017018310_10x_t48',
             'LE_20170627_InCell2000_plate_2017018309_10x_t48',
             'LE_20170627_InCell2000_plate_2017018308_10x_t48',
             'LE_20170627_InCell2000_plate_2017018307_10x_t48',
             'LE_20170627_InCell2000_plate_2017018306_10x_t48',
             'LE_20170627_InCell2000_plate_2017018305_10x_t48',
             'LE_20170627_InCell2000_plate_2017018304_10x_t48',
             'LE_20170627_InCell2000_plate_2017018303_10x_t48',
             'LE_20170627_InCell2000_plate_2017018302_10x_t48',
             'LE_20170627_InCell2000_plate_2017018301_10x_t48',
             'LE_20170627_InCell2000_plate_2017018300_10x_t48',
             'LE_20170627_InCell2000_plate_2017018299_10x_t48',
             'LE_20170627_InCell2000_plate_2017018298_10x_t48',
             'LE_20170627_InCell2000_plate_2017018297_10x_t48',
             'LE_20170627_InCell2000_plate_2017018296_10x_t48']
sigma = 50

corrector.compute_illumination_mask(plateList, sigma)


# To compute the image of the shading pattern
filename = corrector.settings.illum_file.format(plateList[0], sigma)
corrector.plot(filename)
