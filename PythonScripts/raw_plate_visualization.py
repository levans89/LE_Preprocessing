from pyExplorer.rawDataExplorer import imageprint
import os
pprinter = imageprint.PlatePrinter("W:/2015_09_HTS_LE/code/Global_config/basicSettings.py")

plateNames = []

col_number = 12  # State how many columns you wish to see on each side of the plate. So if you want the whole plate this should be 12

# Levelsets for the images
levelsets = [(813, 3889), (1000, 4050), (175, 3000), (0, 0)]  # Between 0 and 4095 for 2x2 binned image
color_order = ['B', 'G', 'R', 'W']  # Tell colors for channels in the same order. Only options: R for red, G for green, B for blue and W for white

# Size of the crop from the images
crop = 500

# NEW THING LOUISE : now you can choose the channels you want. Either "all" for all channels or say [1,3] for first and third

pprinter(plateList=plateNames,
         col_number=col_number,
         levelsets=levelsets,
         color_order=color_order,
         input_folder=os.path.join("T:\\", "2017"),  # ("W:\\","2015_09_HTS_LE\\","temp_data\\","plating",),
         crop=crop,
         channels=[1, 2, 3])
