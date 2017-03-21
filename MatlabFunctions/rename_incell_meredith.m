% 20160129 Louise Evans
% Purpose: Change all file names of incell screen to AW lab format
% Description of input/output variables
% nametable - table of original and reassigned names from files and manual entry
% filepath_24/48 - filepath to the plates taken at 24h/48h post compound addition
% newnames_24/48 - new names to be assigned to the files as defined as a
% cell array of strings in the script calling this function - should be the
% same length as the old names obtained from the directory.
% record_filepath - location in which to store .mat file documenting the
% changes made to the filenames

% converts well names as 'A - 1(fld 1 wv CFP - CFP).tif' to 'LE_20160216_InCell_plate_2016018051_10X_t24_A1_0001-1.tif'
% converts folder names as 'Altschuler_Greiner384_10x_Glass_2016018034_2016.02.17.18.11.49' to 'LE_20160216_InCell_plate_2016018034_10x_t24'

function [nametable] = rename_incell_LE2(data_path, batch, record_filepath, addcpd_date, MS, initial)

% set filepath for 24h plates, extract folder names
%filepath_24 = fullfile(data_path,batch,'/t24');
filepath = 'C:\Users\LEEvans\Desktop\MK025_GFP-Tau_mCherry_MAP2';
names = dir(filepath);
names = names(3:end);
lg = size(names,1);
separator = '_';

for a = 1:lg;
    img_list{a}=names(a).name;
end;

%incorporate sorttiff_LE2
well_nametable_struct = struct;
img_ext = 'tif';

% t_48
    for b = 1:lg
        img_info = regexpi(img_list(b),'(?<row>^[A-P])\s-\s0?(?<col>\d{1,2})\(fld\s(?<frame>\d)\swv\s(?<channel>\w+)\s-','names');
        ROW = img_info{1}.row;
        COL = img_info{1}.col;
        Frame = sprintf('%04s',img_info{1}.frame);
        WV = img_info{1}.channel;
                
        switch WV
            case 'Blue';
                ch = '1';
            case 'Green';
                ch = '2';
            case 'UV';
                ch = '3';
            otherwise
                error('Unknown fluorescence.');
        end
        well_folder = fullfile(filepath,[ROW COL]);
        if ~exist(well_folder,'dir');
            mkdir(well_folder);
        end
        new_name = [[ROW COL] '_' Frame '-' ch '.' img_ext];
        oldwell = fullfile(filepath,img_list(b));
        newwell = cellstr(fullfile(well_folder,new_name))
        movefile(oldwell{1,1},newwell{1,1});
    end
    
end