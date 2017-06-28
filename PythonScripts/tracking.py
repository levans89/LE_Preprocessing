from pyExplorer.dataExplorer import track
'''
#This is to track what has been done for all plates in microscope hard drive.
'''
tracker = track.DataTracker("W:/2015_09_HTS_LE/Code_LE/Global_config/basicSettingsLocal.py")

# plates = ['LE_20160809_Nikon210X_Fn_plate_2016018130_IF_t48',
#           'LE_20160809_Nikon210X_Fn_plate_2016018133_IF_t48']

# tracker(startingPlate='myfavoriteplate') #tracker(finishingPlate='myfavoriteplate')
# tracker(plateList=plates)

tracker(startingPlate='LE_20170425_InCell2000_plate_2017018171_10x_t48')
