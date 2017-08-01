from pyExplorer.rawDataExplorer import heatmap

# This is to perform quality control without segmentation

mapper = heatmap.RoughHeatmapper("W:\\2015_09_HTS_LE\\Code_LE\\Global_config\\basicSettingsLocal.py")
plates = ["LE_20160809_Nikon210X_Fn_plate_2016018130_IF_t48"]


# Change raw to True to use data from microscope hard drive
# Change channels to eg [3] if you want only the information from the third channel
mapper(plates, raw=False, channels="all")