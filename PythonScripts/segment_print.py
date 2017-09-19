from pyExplorer.rawDataExplorer import imageprint

printer = imageprint.PlatePrinter('W:\\2015_09_HTS_LE\\Code_LE\Global_config\\basicSettingsLocal.py')
levelsets = [(40, 1000), (40, 1000), (40, 1000), (40, 1000)]  # between 0 and 4095 for 2x2 binned image
color_order = ["B", "G", "R", "W"]  # Tell colors for channels in the same order.
# Only options: R for red, G for green, B for blue and W for white

plateList = ['LE_20170209_nikon210X_plate_2017018105_t48']
col_number = 4
