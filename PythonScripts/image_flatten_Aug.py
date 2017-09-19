import sys
sys.path.insert(0, 'W:\PyCommonLibrary\pysrc')
from pyExplorer.rawDataExplorer import imageprint
import os, shutil

printer = imageprint.ImagePrinter('W:\\2015_09_HTS_LE\\Code_LE\Global_config\\basicSettingsLocal.py')
levelsets = [(40, 800), (40, 800), (40, 800), (40, 800)]  # between 0 and 4095 for 2x2 binned image
color_order = ["B", "G", "R", "W"]  # Tell colors for channels in the same order.
# Only options: R for red, G for green, B for blue and W for white
crop = 1024

plateNames = ['LE_20170425_InCell2000_plate_2017018173_10x_t48']
wells = ['J20']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018174_10x_t48']
wells = ['A10', 'B5', 'J5', 'F18', 'N20']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018175_10x_t48']
wells = ['P6']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018176_10x_t48']
wells = ['G19', 'C14', 'N9']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018177_10x_t48']
wells = ['B20', 'G4', 'B13', 'B16']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018178_10x_t48']
wells = ['H8', 'P16']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018179_10x_t48']
wells = ['M5', 'A10', 'F15']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018180_10x_t48']
wells = ['A19', 'G4']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018181_10x_t48']
wells = ['L5', 'N17']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018182_10x_t48']
wells = ['A11', 'L21', 'N16']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018183_10x_t48']
wells = ['F17', 'J13', 'I11', 'H20']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018184_10x_t48']
wells = ['E22', 'L4']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018186_10x_t48']
wells = ['P9', 'B5', 'P10']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018187_10x_t48']
wells = ['E11', 'I19', 'C14', 'L15']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018188_10x_t48']
wells = ['E18']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018189_10x_t48']
wells = ['B4']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018190_10x_t48']
wells = ['B5', 'A5', 'A13', 'C19']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018191_10x_t48']
wells = ['I13', 'K18', 'B13', 'D22']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018192_10x_t48']
wells = ['E5']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018193_10x_t48']
wells = ['G12']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018194_10x_t48']
wells = ['E19', 'C8', 'H9']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018195_10x_t48']
wells = ['M21', 'A18', 'H19']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170425_InCell2000_plate_2017018197_10x_t48']
wells = ['B11', 'B13', 'J8']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

####################################################################################### 20170502
plateNames = ['LE_20170502_InCell2000_plate_2017018205_10x_t48']
wells = ['A9', 'G13', 'B6', 'D10']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170502_InCell2000_plate_2017018208_10x_t48']
wells = ['B20']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170502_InCell2000_plate_2017018215_10x_t48']
wells = ['N9']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170502_InCell2000_plate_2017018216_10x_t48']
wells = ['P21']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170502_InCell2000_plate_2017018217_10x_t48']
wells = ['P22']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170502_InCell2000_plate_2017018220_10x_t48']
wells = ['J6']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170502_InCell2000_plate_2017018221_10x_t48']
wells = ['O15', 'N16']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170502_InCell2000_plate_2017018222_10x_t48']
wells = ['C20', 'E20', 'G20', 'I20', 'K20', 'N3']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170502_InCell2000_plate_2017018223_10x_t48']
wells = ['E6']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170502_InCell2000_plate_2017018226_10x_t48']
wells = ['K21']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

##################################################################### 20170515

plateNames = ['LE_20170515_InCell2000_plate_2017018236_10x_t48']
wells = ['M7', 'A16', 'G8', 'D21', 'F17', 'P3']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018238_10x_t48']
wells = ['K9']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018239_10x_t48']
wells = ['A17', 'O3', 'J5', 'P5', 'F20', 'J22']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018241_10x_t48']
wells = ['G13']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018242_10x_t48']
wells = ['H21']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018243_10x_t48']
wells = ['N8']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018244_10x_t48']
wells = ['J18']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018246_10x_t48']
wells = ['M18']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018247_10x_t48']
wells = ['M3', 'I16']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018250_10x_t48']
wells = ['L3']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018251_10x_t48']
wells = ['B4']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018252_10x_t48']
wells = ['O10', 'F19', 'B12', 'H4', 'N4']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018253_10x_t48']
wells = ['O15', 'F15']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018254_10x_t48']
wells = ['K4', 'H21', 'H6']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018255_10x_t48']
wells = ['E20', 'B3', 'F21']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018256_10x_t48']
wells = ['G5', 'H11']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018257_10x_t48']
wells = ['G16', 'I6']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018258_10x_t48']
wells = ['A12']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170515_InCell2000_plate_2017018259_10x_t48']
wells = ['O5']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

############################################################# 20170523

plateNames = ['LE_20170523_InCell2000_plate_2017018266_10x_t48']
wells = ['L7']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018268_10x_t48']
wells = ['A13', 'P3']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018269_10x_t48']
wells = ['A19', 'O17', 'A20', 'O8', 'H17', 'P3']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018270_10x_t48']
wells = ['C3', 'K12', 'K18', 'D13']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018272_10x_t48']
wells = ['G13', 'O3', 'N15', 'P3', 'P21', 'L16']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018273_10x_t48']
wells = ['C19', 'P3', 'P17']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018274_10x_t48']
wells = ['O15', 'I8', 'D5', 'H13', 'P8']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018275_10x_t48']
wells = ['C8', 'L7', 'N17', 'F4']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018276_10x_t48']
wells = ['E21', 'I9', 'B3']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018277_10x_t48']
wells = ['M14']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018278_10x_t48']
wells = ['C18', 'G18', 'D19']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018280_10x_t48']
wells = ['E20', 'O14', 'J16']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018281_10x_t48']
wells = ['O17', 'M22', 'P3', 'P22']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018282_10x_t48']
wells = ['M11', 'I18', 'K12', 'B19', 'L3', 'P13', 'F12']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018283_10x_t48']
wells = ['C13', 'K21', 'P5']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018284_10x_t48']
wells = ['I13', 'K9', 'C16', 'O18', 'L21', 'B10']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018285_10x_t48']
wells = ['A3', 'A9', 'I21', 'O19', 'I18', 'B19', 'L13', 'F12', 'J12', 'P18']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018286_10x_t48']
wells = ['M13', 'O3', 'C14', 'M12', 'B17', 'H15', 'L19', 'B8']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018287_10x_t48']
wells = ['A15', 'G9', 'M5', 'O17', 'F16']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018288_10x_t48']
wells = ['A5', 'I19', 'M15', 'M21', 'M18', 'D19', 'L19', 'P3', 'J12']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170523_InCell2000_plate_2017018289_10x_t48']
wells = ['A15', 'O17', 'A4', 'A8', 'C4', 'E4', 'M4', 'D19', 'J7']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

############################################################# 20170627

plateNames = ['LE_20170627_InCell2000_plate_2017018299_10x_t48']
wells = ['E17', 'D19']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170627_InCell2000_plate_2017018300_10x_t48']
wells = ['N20']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170627_InCell2000_plate_2017018301_10x_t48']
wells = ['H16']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170627_InCell2000_plate_2017018304_10x_t48']
wells = ['K18']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170627_InCell2000_plate_2017018306_10x_t48']
wells = ['C13']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170627_InCell2000_plate_2017018307_10x_t48']
wells = ['M16']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170627_InCell2000_plate_2017018310_10x_t48']
wells = ['M20']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170627_InCell2000_plate_2017018312_10x_t48']
wells = ['P18', 'P16', 'P11', 'P21', 'P19', 'P17', 'P15', 'P13', 'P9', 'P7', 'P22', 'P20', 'P14', 'P12', 'P10', 'P8']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170627_InCell2000_plate_2017018313_10x_t48']
wells = ['L12']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170627_InCell2000_plate_2017018314_10x_t48']
wells = ['F7', 'C6']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170627_InCell2000_plate_2017018319_10x_t48']
wells = ['O15']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170627_InCell2000_plate_2017018320_10x_t48']
wells = ['C16']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170627_InCell2000_plate_2017018321_10x_t48']
wells = ['D20']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170627_InCell2000_plate_2017018323_10x_t48']
wells = ['G16', 'E18']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170627_InCell2000_plate_2017018327_10x_t48']
wells = ['I20']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170627_InCell2000_plate_2017018328_10x_t48']
wells = ['I16']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170627_InCell2000_plate_2017018329_10x_t48']
wells = ['I22']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170627_InCell2000_plate_2017018330_10x_t48']
wells = ['B13']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

############################################################################## 20170628

plateNames = ['LE_20170628_InCell2000_plate_2017018339_10x_t48']
wells = ['I19', 'A5']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018340_10x_t48']
wells = ['B5']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018342_10x_t48']
wells = ['C7', 'C5', 'P13', 'P8']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018343_10x_t48']
wells = ['P12']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018345_10x_t48']
wells = ['O6', 'G8', 'P20']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018349_10x_t48']
wells = ['E21', 'P15', 'F14']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018350_10x_t48']
wells = ['O21']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018351_10x_t48']
wells = ['B15']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018352_10x_t48']
wells = ['C17', 'A15', 'A5', 'I6', 'P3']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018354_10x_t48']
wells = ['L21', 'J5', 'B7', 'F22']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018355_10x_t48']
wells = ['M20']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018356_10x_t48']
wells = ['J3', 'F13']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018357_10x_t48']
wells = ['F19']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018359_10x_t48']
wells = ['K7', 'O20', 'C6', 'E22', 'B9', 'N8']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018361_10x_t48']
wells = ['O13', 'A9', 'P11']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018363_10x_t48']
wells = ['I20']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018365_10x_t48']
wells = ['O13', 'E19', 'J11', 'F15', 'N20']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018366_10x_t48']
wells = ['N17']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018367_10x_t48']
wells = ['D9']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018368_10x_t48']
wells = ['L17']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plateNames = ['LE_20170628_InCell2000_plate_2017018376_10x_t48']
wells = ['P20']
printer.image_print(plateList=plateNames, wellList=wells, levelsets=levelsets, color_order=color_order, channels="all",
                    crop=crop, output_folder='W:\\2015_09_HTS_LE\\results\Images\\Selleck_Bioactives_337_hits')

plates = [d for d in os.listdir('W:\\2015_09_HTS_LE\\results\\Images\\Selleck_Bioactives_337_hits') if os.path.isdir(os.path.join('W:\\2015_09_HTS_LE\\results\\Images\\Selleck_Bioactives_337_hits', d))]
for plate in plates:
    plots = os.listdir(os.path.join('W:\\2015_09_HTS_LE\\results\\Images\\Selleck_Bioactives_337_hits', plate))
    for plot in plots:
        shutil.move(os.path.join('W:\\2015_09_HTS_LE\\results\\Images\\Selleck_Bioactives_337_hits', plate, plot), 'W:\\2015_09_HTS_LE\\results\\Images\\Selleck_Bioactives_337_hits')

