from pyExplorer.rawDataExplorer import imageprint

printer = imageprint.ImagePrinter("../CD_Tag_Drug_Screen/pysrc/pyExplorer/settings/basicSettings_Louise.py")

plateNames = []
wells = []
levelsets=[] #between 0 and 4095 for 2x2 binned image
color_order=[]#Tell colors for channels in the same order. Only options: R for red, G for green, B for blue and W for white

#NEW THING LOUISE : now you can choose the channels you want. Either "all" for all channels or say [1,3] for first and third

printer(plateList = plateNames, wellList = wells, levelsets = levelsets, color_order=color_order, channels="all")


#plateNames = ["LE_20160915_Nikon2_plate_2016018145_IF_t48"]
#wells = ["D4","E4","F4","G4","H4","I4","I9","J9","K9","L9","M9","O9","H21","I21","J21","K21","L21","M21","H10","H11","H12","B2","D2","E2","J3","K3","L3","N13","O13","P13", "A4","B4","C4","A5","B5","C5","A21","B21","C21","C1","D1","M1","N1","C24","D24","M24","N24","O9","P9"] #["A2","B2","C2","D2","E2","F2","G2","H2","I3","J3","K3","L3","M3","N3","O3","P3","H10","H12"]
#levelsets=[(40,2000), (40,1000), (40,2000), (40,2000)] #between 0 and 4095 for 2x2 binned image
#color_order=['B', 'R', 'W', 'G']#Tell colors for channels in the same order. Only options: R for red, G for green, B for blue and W for white

#plateNames = ["LE_20160915_Nikon2_plate_2016018143_IF_t48","LE_20160915_Nikon2_plate_2016018146_IF_B_t48"]
#wells = ["D4","E4","F4","G4","H4","I4","I9","J9","K9","L9","M9","O9","H21","I21","J21","K21","L21","M21","H10","H11","H12","B2","D2","E2","J3","K3","L3","A4","B4","C4","A5","B5","C5","C1","D1","M1","N1","C24","D24","M24","N24","O9","P9"] #["A2","B2","C2","D2","E2","F2","G2","H2","I3","J3","K3","L3","M3","N3","O3","P3","H10","H12"]
#levelsets=[(40,1000), (40,1000), (40,2000), (40,1000)] #between 0 and 4095 for 2x2 binned image
#color_order=['B', 'R', 'W', 'G']#Tell colors for channels in the same order. Only options: R for red, G for green, B for blue and W for white
