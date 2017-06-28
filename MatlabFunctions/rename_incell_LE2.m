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

function [nametable] = rename_incell_LE2(data_path, batch, addcpd_date, MS, initial)

filepath_48 = fullfile(data_path,batch);
display(filepath_48)
names_48 = dir(filepath_48{1,1});
if strcmp(batch{1,1},'2017018_002')==1
names_48 = names_48(3:31);
else 
names_48 = names_48(3:end);
end
nametable_48 = cell((size(names_48,1)),2);
nametable_headers = {'oldnames','newnames'};

% write old names into table from directory
separator = '_';
original_name_headers = {'Lab','Plate','Mag','Mat','Barcode','Timestamp'};
original_name_48 = cell(size(nametable_48,1),1);

%t_48
for j= 1:size(nametable_48,1)
    nametable_48(j,1) = {names_48(j).name};
end
for m = 1:size(nametable_48,1)
    str = nametable_48(m,1);
    original_name_48(m,:) = regexp(str, separator,'split');
end
for n = 1:size(original_name_48,1)
    original_name3(n) = (cell2struct(original_name_48{n,1},original_name_headers,2));
end

original_name_48 = original_name3;
clear original_name3

% construct new platename
% Example format: LE_20160126_InCell_plate_2016018001_10X_t24
plate = 'plate';

if strcmp(batch{1,1},'2017018_003')==1
    [original_name_48.OriginalBarcode] = original_name_48.Barcode; original_name_48 = orderfields(original_name_48,[1:4,7,5:6]); original_name_48 = rmfield(original_name_48,'Barcode');
    original_name_48(1).unnamed = '2017018201';% create new variable
    [original_name_48.Barcode] = original_name_48.unnamed; original_name_48 = orderfields(original_name_48,[1:6,8,7:7]); original_name_48 = rmfield(original_name_48,'unnamed');
    original_name_48(2).Barcode = '2017018202';
    original_name_48(3).Barcode = '2017018204';
    original_name_48(4).Barcode = '2017018205';
    original_name_48(5).Barcode = '2017018206';
    original_name_48(6).Barcode = '2017018207';
    original_name_48(7).Barcode = '2017018208';
    original_name_48(8).Barcode = '2017018210';
    original_name_48(9).Barcode = '2017018211';
    original_name_48(10).Barcode = '2017018212';
    original_name_48(11).Barcode = '2017018214';
    original_name_48(12).Barcode = '2017018215';
    original_name_48(13).Barcode = '2017018216';
    original_name_48(14).Barcode = '2017018218';
    original_name_48(15).Barcode = '2017018220';
    original_name_48(16).Barcode = '2017018222';
    original_name_48(17).Barcode = '2017018224';
    original_name_48(18).Barcode = '2017018226';
    original_name_48(19).Barcode = '2017018228';
    original_name_48(20).Barcode = '2017018230';
    original_name_48(21).Barcode = '2017018203';
    original_name_48(22).Barcode = '2017018209';
    original_name_48(23).Barcode = '2017018213';
    original_name_48(24).Barcode = '2017018217';
    original_name_48(25).Barcode = '2017018219';
    original_name_48(26).Barcode = '2017018221';
    original_name_48(27).Barcode = '2017018223';
    original_name_48(28).Barcode = '2017018225';
    original_name_48(29).Barcode = '2017018227';
    original_name_48(30).Barcode = '2017018229';
elseif strcmp(batch{1,1},'2017018_002')==1
    original_name_48(1).Barcode = '2017018195';
elseif strcmp(batch{1,1},'2017018_005')==1
    original_name_48(15).Barcode = '2017018265';
    original_name_48(16).Barcode = '2017018267';
    original_name_48(17).Barcode = '2017018269';
    original_name_48(18).Barcode = '2017018273';
    original_name_48(19).Barcode = '2017018275';
    original_name_48(20).Barcode = '2017018277';
    original_name_48(21).Barcode = '2017018279';
    original_name_48(22).Barcode = '2017018281';
    original_name_48(23).Barcode = '2017018283';
    original_name_48(24).Barcode = '2017018285';
    original_name_48(25).Barcode = '2017018287';
    original_name_48(26).Barcode = '2017018289';
    original_name_48(27).Barcode = '2017018291';
    original_name_48(28).Barcode = '2017018293';
end

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
for x=2:size(nametable_48,1)
    cd(filepath_48{1,1});
    movefile(nametable_48{x,1},nametable_48{x,2});
end

%incorporate sorttiff_LE2
well_nametable_struct = struct;
img_ext = 'tif';

% t_48
for a = 1:size(nametable_48,1)
    display(nametable_48{a,2});
    img_list = dir(fullfile(filepath_48{1,1},nametable_48{a,2},['*.' img_ext]));
    base_name = (nametable_48{a,2});
    well_nametable_48 = cell(size(img_list,1),2);
    for b = 1:size(img_list,1)
        % parse file name
        img_info = regexpi(img_list(b).name,'(?<row>^[A-P])\s-\s0?(?<col>\d{1,2})\(fld\s(?<frame>\d)\swv\s(?<channel>\w+)\s-','names');
        ROW = upper(img_info.row);
        COL = img_info.col;
        Frame = sprintf('%04s',img_info.frame);
        WV = img_info.channel;
        
        switch WV
            case 'CFP'
                ch = '1';
            case 'TexasRed'
                ch = '3';
            case 'YFP'
                ch = '2';
            otherwise
                error('Unknown fluorescence.');
        end
        well_folder = fullfile(data_path,batch,base_name,[ROW COL]);
        if ~exist(well_folder{1,1},'dir')
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