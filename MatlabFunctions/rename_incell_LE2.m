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
filepath_48 = fullfile(data_path,batch);
%display(filepath_24)
display(filepath_48)
%names_24 = dir(filepath_24{1,1});
names_48 = dir(filepath_48{1,1});
%names_24 = names_24(3:end);
names_48 = names_48(3:end);
lg = size(names_48,1);
nametable_48 = cell(lg,2);
nametable_headers = {'oldnames','newnames'};

% write old names into table from directory
separator = '_';
original_name_headers = {'Lab','Plate','Mag','Mat','Barcode','Timestamp'};
original_name_48 = cell(size(nametable_48,1),1);

%t_48
for j= 1:length(nametable_48)
    nametable_48(j,1) = {names_48(j).name};
end
for m = 1:length(nametable_48)
    str = nametable_48(m,1);
    original_name_48(m,:) = regexp(str, separator,'split');
end
for n = 1:length(original_name_48)
    original_name3(n) = (cell2struct(original_name_48{n,1},original_name_headers,2));
end

original_name_48 = original_name3;
clear original_name3

% construct new platename
% Example format: LE_20160126_InCell_plate_2016018001_10X_t24
plate = 'plate';
nametable_48 = cell(size(original_name_48,2),2);

for o = 1:size(original_name_48,2)
    t = 't48';
    barcode = original_name_48(o).Barcode;
    Mag = original_name_48(o).Mag;
    nametable_48{o,1} = names_48(o).name;
    nametable_48(o,2) = strcat(initial,'_',addcpd_date,'_',MS,'_',plate,'_',barcode,'_',Mag,'_',t);
end

% pause to check input and output will be correct
nametable = vertcat(nametable_headers,nametable_48);
display(nametable)
 

% run movefile function to rename all the folders
for x=12:size(nametable_48,1);
    cd(filepath_48{1,1});
    movefile(nametable_48{x,1},nametable_48{x,2});
end

%incorporate sorttiff_LE2
well_nametable_struct = struct;
img_ext = 'tif';

% t_48
for a = 1:size(nametable_48,1);
    display(nametable_48{a,2});
    img_list = dir(fullfile(filepath_48{1,1},nametable_48{a,2},['*.' img_ext]));
    base_name = (nametable_48{a,2});
    well_nametable_48 = cell(size(img_list,1),2);
    for b = 1:size(img_list,1);
        % parse file name
        img_info = regexpi(img_list(b),'(?<row>^[A-P])\s-\s0?(?<col>\d{1,2})\(fld\s(?<frame>\d)\swv\s(?<channel>\w+)\s-','names');
        ROW = upper(img_info(b).row);
        COL = img_info.col;
        Frame = sprintf('%04s',img_info.frame);
        WV = img_info.channel;
        
        % OLD CODE FOR FORTMAT BEFORE SOFTWARE UPGRADE - A1 not A01
        %         % 1. get row
        %         ROW = img_list(b).name(1);
        %         % 2. get column
        %         COL = regexpi(img_list(b).name,'-\s(\d+)','tokens');
        %         COL = COL{1}{1};
        %         % 3. get frame;
        %         Frame = regexpi(img_list(b).name,'fld\s(\d)\swv','tokens');
        %         Frame = sprintf('%04s',Frame{1}{1});
        %         % 4. get channel
        %         WV = regexpi(img_list(b).name,'wv\s(\w+)\s-','tokens');
        %         WV = WV{1}{1};
        
        switch WV
            case 'CFP';
                ch = '1';
            case 'TexasRed';
                ch = '3';
            case 'YFP';
                ch = '2';
            otherwise
                error('Unknown fluorescence.');
        end
        well_folder = fullfile(data_path,batch,base_name,[ROW COL]);
        if ~exist(well_folder{1,1},'dir');
            mkdir(well_folder{1,1});
        end
        %example of naming convention:             LE_20160126_InCell_plate_2016018001_10X_t24_A1_0001-1.tif
        new_name = [base_name '_' [ROW COL] '_' Frame '-' ch '.' img_ext];
        new_name = strrep(new_name, 'x', 'X');
        %example of generated name from new_name = LE_20160202_InCell_plate_2016018013_10x_t24_A1_0001-1.tif
        well_nametable_48{b,2} = new_name;
        well_nametable_48{b,1} = (img_list(b).name);
        oldwell = fullfile(data_path,batch,base_name,img_list(b).name);
        movefile(oldwell{1,1},fullfile(well_folder{1,1},new_name));
    end
    well_nametable_struct.(nametable_48{a,2})=well_nametable_48;
end

end