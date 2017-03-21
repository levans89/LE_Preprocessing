from pyExplorer.rawDataExplorer import imageprint

pprinter = imageprint.PlatePrinter(
"W:\\2015_09_HTS_LE\\Code\\Global_config\\basicSettings_LE.py")

plateNames =['LE_20160628_Nikon1Fixed10X_plate_2016018090_t48']

col_number = 12 #State how many columns you wish to see on each side of the plate. So if you want the whole plate this should be 12


#Levelsets for the images
levelsets=[(0,2000), (0,2000), (0,2000), (0,0)] #between 0 and 4095 for 2x2 binned image
color_order=['B','G','R','W']#Tell colors for channels in the same order. Only options: R for red, G for green, B for blue and W for white

#Size of the crop from the images
crop=500

#NEW THING LOUISE : now you can choose the channels you want. Either "all" for all channels or say [1,3] for first and third
pprinter(plateList = plateNames, col_number=col_number, levelsets = levelsets, color_order=color_order, crop=crop, channels=[1,2,3])
