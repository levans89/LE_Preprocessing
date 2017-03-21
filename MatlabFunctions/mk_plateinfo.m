% Louise Evans March 2016
% replace function of labtoolbox so that batches are quicker to process.

function [P] = mk_plateinfo(currexp,cpd_DB,plate_infopath)

expression = 'plate_';
expression2 = '_'
prefix = 'plateindex_';

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
P_template.Mtype= 'Nikon II';% InCell 2000, Nikon I, Nikon II
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

for a =1:size(img_folders,2)
    P = P_template;
    splitname_plate = regexp(img_folders(a),expression,'split');
    splitname_plate2 = regexp(img_folders(a),expression2,'split');
    subname_plate = splitname_plate{1,1}{1,2};
    P.plate = subname_plate;
    P.title = img_folders{a,1};
    p = strcat(prefix,subname_plate);
    save(fullfile(plate_infopath,p),'P')
end
end