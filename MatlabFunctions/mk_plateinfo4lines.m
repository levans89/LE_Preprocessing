% Louise Evans March 2017
% replace function of labtoolbox so that batches are quicker to process.

function [P] = mk_plateinfo4lines(currexp,plate_infopath)

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
P_template.Year= 2017;
P_template.markerset2= {'H2B','','CYTO'};
P_template.markerset= {'CFP','YFP','mCHERRY'};
P_template.color= {'B','Y','R'} ;
P_template.nuclMK= 1;%1
P_template.MKFEind= 2;%2
P_template.cytoMK= 3;%3
P_template.range= [0 0 0; 4095 4095 4095];

% rename P_template fields appropriately

for a = 1:size(currexp,1)
    P = P_template;
    P.title = currexp.plate_name{a};
    P.plate = strcat((currexp.expt_plate{a}),'_',(currexp.timepoint{a}));
    P.Ctype = currexp.CellLine{a};
    TF = strcmp(currexp.markertype{a,1},'MEDIA')
    if TF == 1
        P.markerset2{2}='MEDIA'
    else
        P.markerset2{2}=currexp.markertype{a,1}{1,2}
    end
    p = strcat(prefix,P.plate);
    save(fullfile(plate_infopath,p),'P')
end
end