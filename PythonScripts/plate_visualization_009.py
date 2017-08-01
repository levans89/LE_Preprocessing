from pyExplorer.rawDataExplorer import imageprint

pprinter = imageprint.PlatePrinter("W:\\2015_09_HTS_LE\\Code_LE\\Global_config\\basicSettingsLocal.py")


plateNames = ['LE_20170719_InCell2000_plate_2017018396_10x_t48',
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
              'LE_20170719_InCell2000_plate_2017018377_10x_t48',
              'LE_20170719_InCell2000_plate_2017018398_10x_t48',
              'LE_20170719_InCell2000_plate_2017018397_10x_t48']
#    'LE_20170719_InCell2000_plate_2017018399_10x_t48',]

col_number = 2  # State how many columns you wish to see on each side of the plate. So if you want the whole plate this should be 12


# Levelsets for the images
levelsets = [(40, 1000), (40, 1000), (40, 1000), (40, 1000)]  # between 0 and 4095 for 2x2 binned image
color_order = ['B', 'G', 'R', 'W']  # Tell colors for channels in the same order. Only options: R for red, G for green, B for blue and W for white

# Size of the crop from the images
crop = 1024

# NEW THING LOUISE : now you can choose the channels you want. Either "all" for all channels or say [1,3] for first and third
pprinter.plateprint(plateList=plateNames, col_number=col_number, levelsets=levelsets, color_order=color_order, crop=crop, channels=[1, 2, 3])
