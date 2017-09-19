from pyExplorer.rawDataExplorer import imageprint
import pandas as pd
import os
import sys
import shutil
sys.path.insert(0, 'W:\\2015_09_HTS_LE\\Code_LE\\Global_config')
import basicSettingsLocal_Image_flatten

printer = imageprint.ImagePrinter(
    'W:\\2015_09_HTS_LE\\Code_LE\Global_config\\basicSettingsLocal_Image_flatten.py')
levelsets = [(40, 1000), (40, 1000), (40, 1000), (40, 1000)]  # between 0 and 4095 for 2x2 binned image
color_order = ["B", "G", "R", "W"]  # Tell colors for channels in the same order.
crop = 300
hit_list = pd.read_excel('W:\\2015_09_HTS_LE\\results\\Images\\Selleck_Bioactives\\hit_list_XRCC5_2K.xlsx')

lst_cluster_folders = []
def image_flatten_clusters(wells, plateNames):
    # sorting into folders by cluster
    plateNames_string = plateNames[0]
    plateID = plateNames_string[plateNames_string.find('plate') + 6:plateNames_string.find('plate') + 6 + 10] # extract the plate ID from plateNames
    for well in wells:
        for x in range(0, 537):
                if plateID == str(hit_list.iloc[x, 3]) and well == hit_list.iloc[x, 4]:
                    cluster = hit_list.iloc[x, 0]
                    newpath = 'W:\\2015_09_HTS_LE\\results\\Images\\Selleck_Bioactives\\Cluster_' + '{}'.format(cluster)
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
                    if newpath not in lst_cluster_folders:
                        lst_cluster_folders.append(newpath)
                    printer.image_print(plateList=plateNames, wellList=[well], levelsets=levelsets,
                                        color_order=color_order, channels=["all"],
                                        crop=crop, output_folder=newpath)
    # save images directly into Cluster folder, instead of in plate name sub-folders:
    for Cluster_folder in lst_cluster_folders:
        plates = [d for d in os.listdir(Cluster_folder) if os.path.isdir(os.path.join(Cluster_folder, d))]
        for plate in plates:
            plots = os.listdir(os.path.join(Cluster_folder, plate))
            for plot in plots:
                shutil.move(os.path.join(Cluster_folder, plate, plot), Cluster_folder)
            # os.remove(os.path.join(Cluster_folder, plate))

lst_pathway_folders = []
def image_flatten_pathways(wells, plateNames):
    # sorting into folders by pathway
    plateNames_string = plateNames[0]
    plateID = plateNames_string[plateNames_string.find('plate') + 6:plateNames_string.find('plate') + 6 + 10] # extract the plate ID from plateNames
    for well in wells:
        for x in range(0, 537):
                if plateID == str(hit_list.iloc[x, 3]) and well == hit_list.iloc[x, 4]:
                    pathway = hit_list.iloc[x, 10]
                    newpath = 'W:\\2015_09_HTS_LE\\results\\Images\\Selleck_Bioactives\\Pathway_{}'.format(pathway)
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
                    if newpath not in lst_pathway_folders:
                        lst_pathway_folders.append(newpath)
                    printer.image_print(plateList=plateNames, wellList=well, levelsets=levelsets,
                                        color_order=color_order, channels=["all"],
                                        crop=crop, output_folder=newpath)
    # save images directly into Pathway folder, instead of in plate name sub-folders
    for Pathway_folder in lst_pathway_folders:
        plates = [d for d in os.listdir(Pathway_folder) if os.path.isdir(os.path.join(Pathway_folder, d))]
        for plate in plates:
            plots = os.listdir(os.path.join(Pathway_folder, plate))
            for plot in plots:
                shutil.move(os.path.join(Pathway_folder, plate, plot), Pathway_folder)
            # os.remove(os.path.join(Pathway_folder, plate))

def run(wells, plateNames):
    image_flatten_clusters(wells, plateNames)
    image_flatten_pathways(wells, plateNames)

# 2017018105
plateNames = ['LE_20170209_nikon210X_plate_2017018105_t48']
wells = ['A2']
run(wells, plateNames)
'''
# 2017018104
plateNames = ['LE_20170209_nikon210X_plate_2017018104_t48']
wells = ['A16', 'E7','C5','N3','I3']
run(wells, plateNames)

# 2017018089
plateNames = ['LE_20170211_nikon210X_plate_2017018089_t48']
wells = ['M12', 'K4','K15', 'K9']
run(wells, plateNames)

#  2017018086
plateNames = ['LE_20170211_nikon210X_plate_2017018086_t48']
wells = ['B10', 'H8', 'N22', 'H11', 'D15', 'L9']
run(wells, plateNames)

# 2017018081
plateNames = ['LE_20170210_nikon210X_plate_2017018081_t48']
wells = ['G9', 'K21','A13','M13']
run(wells, plateNames)

#  2017018079
plateNames = ['LE_20170210_nikon210X_plate_2017018079_t48']
wells = ['O5', 'B5', 'E11', 'G16', 'G12', 'A17','M3']
run(wells, plateNames)

'''