% Louise Evans 20160120
% Purpose: combine separate files for same drug library into one file, one has platemap info, other has database IDs.

% example filepath1 = './Drug libaries/DIVIV-NCI-Diversity-1430-AW.xlsx';
% example filepath2 = './Drug libaries/DIVIV-NCI-Diversity-1430-AW_map.xlsx';


function [combo_library] = LE_combineNCI_DIVIV_info (filepath1,filepath2)

% read in num txt raw versions of each file
[combo_library.num, ~, combo_library.raw] = xlsread(filepath1);
[combo_library.num2,~, combo_library.raw2] = xlsread(filepath2);

% define whether the two are overlapping
[~,combo_library.idx] = ismember(combo_library.num2(:,3),combo_library.num(:,1));

% use logical indexing to find where file 1 is present in file 2
combo_library.idx(~combo_library.idx)=length(combo_library.num)+1;% make values not present equal to numeric value one longer than num 
combo_library.num(length(combo_library.num)+1,1)= 0; % add last term to first array and make the value equal to 0. 

for i=1:length(combo_library.num2);%for each of second array
    j = combo_library.idx(i,1);% assign a value to j using index value from array 1
    combo_library.num2(i,4)= combo_library.num(j,2);% use that index value to assign the value to array 2 in the correct location
end

combo_library.num = combo_library.num(1:length(combo_library.num)-1,:);% remove that extra one you added at line 18
% append headers to raw files
combo_library.raw2(1,4)=combo_library.txt(1,2);

% write combo library into raw file from num file
for k=2:length(combo_library.raw2);% 2 because first row is header
    combo_library.raw2(k,4)={combo_library.num2(k-1,4)};% k-1 because without headers num array is shifted
end

% clean up
clear i j k

% write combinded file to Excel sheet in same folder as you got the files
% from
xlswrite('./Drug libaries/DIVIV-NCI-Diversity-1430-AW_combined.xlsx',combo_library.raw2);
end

