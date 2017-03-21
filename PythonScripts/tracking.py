from pyExplorer.dataExplorer import track
'''
#This is to track what has been done for all plates in microscope hard drive.
'''
tracker = track.DataTracker("W:/2015_09_HTS_LE/code/Global_config/basicSettings_LE.py")

# plates = ['LE_20160809_Nikon210X_Fn_plate_2016018130_IF_t48',
#           'LE_20160809_Nikon210X_Fn_plate_2016018133_IF_t48',
#           'LE_20160809_Nikon210X_Fn_plate_2016018132_IF_t48',
#           'LE_20160809_Nikon210X_Fn_plate_2016018134_IF_t48']

#plates = ["LE_20160915_Nikon2_plate_2016018146_IF_B_t48", "LE_20160915_Nikon2_plate_2016018143_IF_t48", "LE_20160915_Nikon2_plate_2016018144_IF_t48", "LE_20160915_Nikon2_plate_2016018145_IF_t48"]


#tracker(startingPlate='myfavoriteplate') #tracker(finishingPlate='myfavoriteplate')
#tracker(plateList=plates)dir

tracker(startingPlate = 'LE_20170209_nikon210X_plate_2017018055_t48')
