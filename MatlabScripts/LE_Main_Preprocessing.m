% Louise Evans January 2016
% Purpose: Main script to analyse data batches
% prerequisites: 
    % update plate_database.xlsx
    % make compound plate maps in project_database/cpd_plate_keys
    % transfer data from incell to Z:\Data_Transfer\incell_screens
% actions: 
% 1. Rename folders from InCell to AW lab protocol using "rename_incell_LE.m"
% 2. Rename folders within files to AW lab protocol "flipdata_LE.m"
% 3. Copy option.mat to folders

%% Set all variables 

% define experimental details
batches = {'2016018_001','2016018_002','2016018_003','2016018_004','2016018_005','2016018_006','2016018_007','2016018_C001', '2016018_C002', '2016018_C003','2016018_C004','2016018C005','2016018_carryover','2017018_001','2017018_003'}';
addcpd_dates = {'20160126','20160202','20160216','20160426','20160503','20160601','20160627','20160627', '20160719', '20160802','20160809','20160906','20161129','20170117','20170207'}';
% standard experimental details for this project
year = '2017';
initial = 'LE';
MS = 'Nikon2' % for plate renaming purposes no spaces
MS2 = 'Nikon II';% Nikon I, Nikon II, InCell 2000 % for plateinfo purposes as set in labtoolbox

%% PC standard datapaths

% add all the paths needed for these codes to run and call matlab functions
%addpath(genpath('W:\2015_09_HTS_LE\code\')) %add code and all subfolders to matlab search path
data_path = 'Z:\Data_Transfer\'; % location of raw data copied from InCell for pre-processing
record_filepath = 'W:\2015_09_HTS_LE\data\processing_history\'; %output for processing history
plate_infopath = 'W:\Common\plateinfo\'; %output for generated plateinfo
platedata_folder = 'W:\2015_09_HTS_LE\plates\'; %directory in which to make individual plate folders by barcode
plate_DB_path ='W:\2015_09_HTS_LE\project_database\';
plate_DB = 'Plate_database_latest.xlsx';
%% 1. Call rename_incell.LE.m
% define the record filepath to record the old and new names

for i = 14 %:length(batches) % index of the batch do you want to analyze or all batches or 
    batch = batches(i,1)
    addcpd_date = addcpd_dates(i,1)
    [nametable] = rename_incell_LE2(data_path, batch, record_filepath, addcpd_date, MS, initial);
end

savepath = 
save(fullfile(record_filepath,batch{1,1}))

%% 2. 20160212LE replace functionality of the labtoolbox plateinfo generation
% Get nametable if using Nikon
nametable = dir()
%% 
%load(fullfile(record_filepath,batch{1,1}))
[P] = set_structures(plate_infopath, nametable, platedata_folder);
%% 3. Make exp plate maps from compound plate maps 
%load(fullfile(record_filepath,batch{1,1}))
for x = 14
exp_anno_maker(batch{x}, plate_DB, year)
end
