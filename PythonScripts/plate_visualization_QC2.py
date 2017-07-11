from pyExplorer.rawDataExplorer import imageprint

pprinter = imageprint.PlatePrinter("W:/2015_09_HTS_LE/code/LE_Preprocessing/PythonScripts/basicSettings_Louise_QC2.py")

plateNames = ['LE_20151203_Nikon_plate_2015018025_20XPH1_t48',
              'LE_20151203_Nikon_plate_2015018022_10XDIC_t24',
              'LE_20151203_Nikon_plate_2015018022_10XDIC_t48',
              'LE_20151203_Nikon_plate_2015018023_10XDIC_t24',
              'LE_20151203_Nikon_plate_2015018023_10XDIC_t48',
              'LE_20151203_Nikon_plate_2015018024_10XDIC_t24',
              'LE_20151203_Nikon_plate_2015018024_10XDIC_t48',
              'LE_20151203_Nikon_plate_2015018025_10XDIC_t24',
              'LE_20151209_Nikon_plate_2015018027_10XDIC_t24',
              'LE_20151209_Nikon_plate_2015018027_10XDIC_t48',
              'LE_20151209_Nikon_plate_2015018027_20XPH1_t24',
              'LE_20151209_Nikon_plate_2015018027_20XPH1_t48',
              'LE_20151209_Nikon_plate_2015018028_10XDIC_t48',
              'LE_20151209_Nikon_plate_2015018028_20XPH1_t24',
              'LE_20151209_Nikon_plate_2015018029_10XDIC_t24',
              'LE_20151209_Nikon_plate_2015018029_10XDIC_t48',
              'LE_20151209_Nikon_plate_2015018029_20XPH1_t24',
              'LE_20151209_Nikon_plate_2015018029_20XPH1_t48',
              'LE_20151209_Nikon_plate_2015018030_10XDIC_t24',
              'LE_20151209_Nikon_plate_2015018030_10XDIC_t48',
              'LE_20151209_Nikon_plate_2015018030_20XPH1_t48',
              'LE_20151209_Nikon_plate_2015018031_10XDIC_t24',
              'LE_20151209_Nikon_plate_2015018031_10XDIC_t48',
              'LE_20151209_Nikon_plate_2015018031_20XPH1_t24',
              'LE_20151209_Nikon_plate_2015018031_20XPH1_t48',
              'LE_20151209_Nikon_plate_2015018032_10XDIC_t24',
              'LE_20151209_Nikon_plate_2015018032_10XDIC_t48',
              'LE_20151209_Nikon_plate_2015018032_20XPH1_t24',
              'LE_20151209_Nikon_plate_2015018032_20XPH1_t48',
              'LE_20151209_Nikon_plate_2015018033_10XDIC_t24',
              'LE_20151209_Nikon_plate_2015018033_10XDIC_t48',
              'LE_20151209_Nikon_plate_2015018033_20XPH1_t24',
              'LE_20151209_Nikon_plate_2015018033_20XPH1_t48',
              'LE_20151203_Nikon_plate_2015018025_10XDIC_t48',
              'LE_20151203_Nikon_plate_2015018025_20XPH1_t24']

col_number = 12  # State how many columns you wish to see on each side of the plate. So if you want the whole plate this should be 12

# Levelsets for the images
levelsets = [(10, 200), (10, 100), (10, 100), (0, 0)]  # Between 0 and 4095 for 2x2 binned image
color_order = ['B', 'G', 'R', 'W']  # Tell colors for channels in the same order. Only options: R for red, G for green, B for blue and W for white

# Size of the crop from the images
crop = 500

# NEW THING LOUISE : now you can choose the channels you want. Either "all" for all channels or say [1,3] for first and third
pprinter(plateList=plateNames, col_number=col_number, levelsets=levelsets, color_order=color_order, crop=crop, channels=[1, 2, 3])
