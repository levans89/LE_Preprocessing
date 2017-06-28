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

%% define experimental details
batches = {'2017018_002', '2017018_003','2017018_004','2017018_005'}'; %{'1','2','3'} Append new each week
addcpd_dates = {'20170425', '20170502','20170515','20170523'}'; %{'1','2','3'} Append new each week
data_path = 'Z:\Data_Transfer\'; % location of raw data copied from InCell for pre-processing

%% PC standard datapaths
% standard experimental details for this project
year = '2017';
initial = 'LE';
MS = 'InCell2000'; % for plate renaming purposes no spaces
MS2 = 'InCell 2000';% Nikon I, Nikon II, InCell 2000 % for plateinfo purposes as set in labtoolbox

% add all the paths needed for these codes to run and call matlab functions
addpath(genpath('W:\2015_09_HTS_LE\Code_LE\LE_Preprocessing'))
addpath(genpath('W:\2015_09_HTS_LE\Code_LE\LE_Analysis'))
addpath(genpath('W:\2015_09_HTS_LE\Code_LE\CD_Tag_Drug_Screen'))%add code and all subfolders to matlab search path
record_filepath = 'W:\2015_09_HTS_LE\data\processing_history\'; %output for processing history
plate_infopath = 'W:\Common\plateinfo\'; %output for generated plateinfo
platedata_folder = 'W:\2015_09_HTS_LE\plates\'; %directory in which to make individual plate folders by barcode
plate_DB_path ='W:\2015_09_HTS_LE\project_database\';
plate_DB = 'Plate_database_latest2.xlsx';

%% 1. Call rename_incell.LE.m
for i = 4 % index of the batch do you want to analyze or all batches
    batch = batches(i,1);
    addcpd_date = addcpd_dates(i,1);
    [nametable] = rename_incell_LE2(data_path, batch, addcpd_date, MS, initial);
    makeQCfiles_LE(batch,plate_DB_path,plate_DB);
end
save(fullfile(record_filepath,batch{1,1})) % Saves record of processing history

%% 2. 20160212LE replace functionality of the labtoolbox plateinfo generation
load(fullfile(record_filepath,batch{1,1}))
[P] = set_structures(plate_infopath, nametable, platedata_folder, MS2);
cd('W:\2015_09_HTS_LE\Code_LE');
%% 3. Make exp plate maps from compound plate maps 
%load(fullfile(record_filepath,batch{1,1}))
% make cpd platemaps
%chembridge_cpdmaps_LE()
for i = 4
batch = batches(i,1);% index of the batch do you want to analyze or all batches
exp_anno_maker(batch{1},plate_DB_path,plate_DB, year)
end
