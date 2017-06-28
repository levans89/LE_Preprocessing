% Louise Evans March 2016
% Purpose: replace function of labtoolbox so that batches are quicker to process.

function [P] = set_structures(plate_infopath, nametable, platedata_folder, MS2)

img_folders = nametable(2:end,2);
expression = 'plate_';
prefix = 'plateindex_';

plates = nametable(2:end,2);

for b = 1:length(plates)% make all the folders and subfolders for each plate in the project/plates folder
    cd(platedata_folder);
    plate_folder = plates{b};
    display(plate_folder)
    if ~exist(plate_folder,'dir')
        mkdir(plate_folder)
        cd(plate_folder)
        mkdir('bgs_images')
        mkdir('cache')
        mkdir('config')
        mkdir('features\cbfeatures')
        mkdir('quality_control')
        mkdir('segmentation')
    end
end

% create P_template for editing - this will form part of the plateinfo.mat
% file
P_template.plate = '';
P_template.comment= '';
P_template.username= 'levans';
P_template.title= '';
P_template.project= '2015_09_HTS_LE';
P_template.binning= 2%2;
P_template.Ctype= '';
P_template.Ptype= 384;
P_template.Mtype= '';% InCell 2000, Nikon I, Nikon II
P_template.Btype= 12;
P_template.Nframe= 1;
P_template.Year= 2016;
P_template.markerset2= {'H2B','XRCC5','CYTO'};
P_template.markerset= {'CFP','YFP','mCHERRY'};
P_template.color= {'B','Y','R'} ;
P_template.nuclMK= 1;%1
P_template.MKFEind= 2;%2
P_template.cytoMK= 3;%3
P_template.range= [0 0 0; 4095 4095 4095];

% rename P_template fields appropriately

for a =1:size(img_folders,1)
    P = P_template;
    splitname_plate = regexp(img_folders(a),expression,'split');
    subname_plate = splitname_plate{1,1}{1,2};
    P.plate = subname_plate;
    P.title = img_folders{a,1};
    P.Mtype = MS2;
    p = strcat(prefix,subname_plate);
    save(fullfile(plate_infopath,p),'P')
end

end