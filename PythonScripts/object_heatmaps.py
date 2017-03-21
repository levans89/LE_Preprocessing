from pyExplorer.dataExplorer.qualityController import heatmap
'''
This is to perform quality control heatmaps based on segmented objects.
'''
mapper = heatmap.ObjectHeatmapper("../CD_Tag_Drug_Screen/pysrc/pyExplorer/settings/basicSettings_Louise.py")

plates = ["LE_20160915_Nikon2_plate_2016018143_IF_t48","LE_20160915_Nikon2_plate_2016018146_IF_B_t48"]
#["LE_20160915_Nikon2_plate_2016018146_IF_B_t48", "LE_20160915_Nikon2_plate_2016018143_IF_t48", "LE_20160915_Nikon2_plate_2016018144_IF_t48", "LE_20160915_Nikon2_plate_2016018145_IF_t48"]
#comments
features = ["pAkt_DIav", 'pAkt_YIav', 'pAkt_RDCIav','B-Tubulin_YIav','pERK_DIav','pERK_YIav']
#["cell_count", "Hoechst_DI50", "B-Tubulin_CI50"]

mapper(plates,features)