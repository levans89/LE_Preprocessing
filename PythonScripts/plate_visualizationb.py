from pyExplorer.rawDataExplorer import imageprint

pprinter = imageprint.PlatePrinter("W:\\2015_09_HTS_LE\\Code_LE\\Global_config\\basicSettingsLocal.py")

#plateNames = ['LE_20170627_InCell2000_plate_2017018333_10x_t48']

# plateNames = ['LE_20170627_InCell2000_plate_2017018333_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018332_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018331_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018330_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018328_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018327_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018326_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018325_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018324_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018323_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018322_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018321_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018320_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018319_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018318_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018317_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018316_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018315_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018314_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018313_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018312_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018311_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018310_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018309_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018308_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018307_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018306_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018305_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018304_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018303_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018302_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018301_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018300_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018299_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018298_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018297_10x_t48',
#               'LE_20170627_InCell2000_plate_2017018296_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018376_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018372_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018371_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018370_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018369_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018368_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018367_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018366_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018365_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018364_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018363_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018362_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018361_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018360_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018359_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018358_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018357_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018356_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018355_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018354_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018352_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018351_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018350_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018349_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018348_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018347_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018346_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018345_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018344_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018343_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018342_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018341_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018340_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018339_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018338_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018337_10x_t48',
#               'LE_20170628_InCell2000_plate_2017018336_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018268_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018270_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018272_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018274_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018276_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018278_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018280_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018282_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018284_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018286_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018288_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018290_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018294_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018265_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018267_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018269_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018273_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018275_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018277_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018279_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018281_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018283_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018285_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018287_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018289_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018291_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018293_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018266_10x_t48']

#               'LE_20170523_InCell2000_plate_2017018265_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018266_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018267_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018268_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018269_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018270_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018272_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018273_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018274_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018275_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018276_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018277_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018278_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018279_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018280_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018281_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018282_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018283_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018284_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018285_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018286_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018287_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018288_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018289_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018290_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018291_10x_t48',
#               'LE_20170523_InCell2000_plate_2017018293_10x_t48']

plateNames = ['LE_20170515_InCell2000_plate_2017018235_10x_t48',
              'LE_20170515_InCell2000_plate_2017018236_10x_t48',
              'LE_20170515_InCell2000_plate_2017018237_10x_t48',
              'LE_20170515_InCell2000_plate_2017018238_10x_t48',
              'LE_20170515_InCell2000_plate_2017018239_10x_t48',
              'LE_20170515_InCell2000_plate_2017018240_10x_t48',
              'LE_20170515_InCell2000_plate_2017018241_10x_t48',
              'LE_20170515_InCell2000_plate_2017018242_10x_t48',
              'LE_20170515_InCell2000_plate_2017018243_10x_t48',
              'LE_20170515_InCell2000_plate_2017018244_10x_t48',
              'LE_20170515_InCell2000_plate_2017018245_10x_t48',
              'LE_20170515_InCell2000_plate_2017018246_10x_t48',
              'LE_20170515_InCell2000_plate_2017018247_10x_t48',
              'LE_20170515_InCell2000_plate_2017018248_10x_t48',
              'LE_20170515_InCell2000_plate_2017018249_10x_t48',
              'LE_20170515_InCell2000_plate_2017018250_10x_t48',
              'LE_20170515_InCell2000_plate_2017018251_10x_t48',
              'LE_20170515_InCell2000_plate_2017018252_10x_t48',
              'LE_20170515_InCell2000_plate_2017018253_10x_t48',
              'LE_20170515_InCell2000_plate_2017018254_10x_t48',
              'LE_20170515_InCell2000_plate_2017018255_10x_t48',
              'LE_20170515_InCell2000_plate_2017018256_10x_t48',
              'LE_20170515_InCell2000_plate_2017018257_10x_t48',
              'LE_20170515_InCell2000_plate_2017018258_10x_t48',
              'LE_20170515_InCell2000_plate_2017018259_10x_t48',
              'LE_20170515_InCell2000_plate_2017018260_10x_t48',
              'LE_20170515_InCell2000_plate_2017018261_10x_t48',
              'LE_20170515_InCell2000_plate_2017018262_10x_t48',
              'LE_20170515_InCell2000_plate_2017018263_10x_t48',
              'LE_20170515_InCell2000_plate_2017018264_10x_t48',
              'LE_20170425_InCell2000_plate_2017018171_10x_t48',
              'LE_20170425_InCell2000_plate_2017018175_10x_t48',
              'LE_20170425_InCell2000_plate_2017018178_10x_t48',
              'LE_20170425_InCell2000_plate_2017018179_10x_t48',
              'LE_20170425_InCell2000_plate_2017018193_10x_t48',
              'LE_20170425_InCell2000_plate_2017018196_10x_t48',
              'LE_20170425_InCell2000_plate_2017018197_10x_t48',
              'LE_20170502_InCell2000_plate_2017018230_10x_t48',
              'LE_20170502_InCell2000_plate_2017018224_10x_t48',
              'LE_20170502_InCell2000_plate_2017018214_10x_t48']

# plateNames = ['LE_20170425_InCell2000_plate_2017018185_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018198_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018214_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018228_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018229_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018227_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018172_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018199_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018200_10x_t48']
# plateNames = ['LE_20170425_InCell2000_plate_2017018173_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018174_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018175_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018176_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018177_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018178_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018179_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018180_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018181_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018182_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018183_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018184_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018186_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018187_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018188_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018189_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018190_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018191_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018192_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018193_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018194_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018196_10x_t48',
#               'LE_20170425_InCell2000_plate_2017018197_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018217_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018226_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018203_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018206_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018212_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018225_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018224_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018213_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018204_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018223_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018201_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018205_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018218_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018208_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018209_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018220_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018215_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018230_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018210_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018202_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018219_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018211_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018221_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018216_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018222_10x_t48',
#               'LE_20170502_InCell2000_plate_2017018207_10x_t48']


col_number = 2  # State how many columns you wish to see on each side of the plate. So if you want the whole plate this should be 12


# Levelsets for the images
levelsets = [(40, 1000), (40, 1000), (40, 1000), (40, 1000)]  # between 0 and 4095 for 2x2 binned image
color_order = ['B', 'G', 'R', 'W']  # Tell colors for channels in the same order. Only options: R for red, G for green, B for blue and W for white

# Size of the crop from the images
crop = 1024

# NEW THING LOUISE : now you can choose the channels you want. Either "all" for all channels or say [1,3] for first and third
pprinter.plateprint(plateList=plateNames, col_number=col_number, levelsets=levelsets, color_order=color_order, crop=crop, channels=[1, 2, 3])
# Taking raw images
pprinter.plateprint(plateList=plateNames, col_number=col_number, levelsets=levelsets, color_order=color_order, crop=crop,
                    channels=[1, 2, 3])
