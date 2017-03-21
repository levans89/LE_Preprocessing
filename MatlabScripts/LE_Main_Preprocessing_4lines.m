% Louise Evans March 2017
% Purpose: preprocessing 4lines experiment
% Prerequisites:
    % project_database_latest.xlsx
    % 4L2K_B1_8.xlsx, 
% Actions:
    % creation of compound and experiment plate maps,
    % create plate directories and subdirectories, plate_info files

    %% path setup and file import
    %====add all the paths needed for these codes to run and call matlab functions====%
    addpath(genpath('W:\2015_09_HTS_LE\code\LE_Preprocessing\')) % add code and all subfolders to matlab search path
    record_filepath = 'W:\2015_09_HTS_LE\data\processing_history\'; % output for processing history
    plate_infopath = 'W:\Common\plateinfo\'; % output for generated plateinfo
    platedata_folder = 'W:\2015_09_HTS_LE\plates\'; % directory in which to make individual plate folders by barcode
    plate_DB_path ='W:\2015_09_HTS_LE\project_database\'; % directory containing plate database file
    plate_DB = 'Plate_database_latest.xlsx'; % file describing relationship between compound and experiment plates
    exp_DB = readtable(fullfile(plate_DB_path,plate_DB),'Sheet', 1);% read in sheet of all physical experiment (cell) plates
    cpd_DB = readtable(fullfile(plate_DB_path,plate_DB),'Sheet', 3); % read in sheet of all physical compound stock plates
    year = '2017' %input to exp_anno...
    
    %% select plateset
    %====select the set of plates to analyze in this experiment as a whole====%
    expt='LE_4'; % references the field Experiment_ in exp_DB
    currexp = getplates(expt, exp_DB);% extract plates from DB of all plates ever screened
    
    %% create platefolders
    %====create plate directories and subdirectories====%
    [~,img_folders,~]=xlsread('W:\2015_09_HTS_LE\project_database\screening notes\4L2K_B1_8.xlsx');% readin all plates of this batch (cleaner file than plate_database_latest.xlsx)
    %set_structures4lines(img_folders, platedata_folder) % replaces functionality of labtoolbox to initialize plates
    
    %% create plateinfo
    %====make all plateinfo files for use in generating profiles later====%
    currexp.markertype=regexp(currexp.CellLine,'_','split'); % split cell line into marker and cell line
    celllines = unique(currexp.CellLine); % list the cell lines
    for y = 1:size(img_folders,1)
        img_folders(y,2:7) = regexp(img_folders{y,1},'_','split'); % split up the complete folder name to pull out sub-names
    end
    img_folders = img_folders(:,[1 6 7]); % rejoin selected parts
    img_folders = cell2table(img_folders);% make table
    img_folders.Properties.VariableNames{2} = 'expt_plate'; %rename variables
    img_folders.Properties.VariableNames{1} = 'plate_name';
    img_folders.Properties.VariableNames{3}= 'timepoint';
    currexp=join(img_folders, currexp); %add actual folder namtes into the table currexp rather than just barcodes
    %[P] = mk_plateinfo4lines(currexp,plate_infopath) % makes plateinfo for each plate (labtoolbox replacement)
    
    %% make compound maps
    %====Create excel files of each compound master plate====%
    [Selleck]=import_compoundplates(); % imports Selleck2K raw compound map
    plateprinter; % makes compound plates in excel in lab agreed format
    
    %% create expt platemaps
    %====Create excel files of each experiment plate====%
    exp_anno_maker4lines(currexp,cpd_DB,year,expt) % makes experimental plates in excel in lab agreed format
    