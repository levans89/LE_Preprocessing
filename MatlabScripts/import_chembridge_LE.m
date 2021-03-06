%% Import data from text file.
% Script for importing data from the following text file:
%
%    W:\2015_09_HTS_LE\project_database\cpd_plate_keys\ChemBridgeV2\ChemBridge-Premium-50k.txt
%
% To extend the code to different selected data or a different text file,
% generate a function instead of a script.

% Auto-generated by MATLAB on 2017/05/17 15:23:34

%% Initialize variables.
filename = 'W:\2015_09_HTS_LE\project_database\cpd_plate_keys\ChemBridgeV2\ChemBridge-Premium-50k.txt';
delimiter = '\t';
startRow = 2;

%% Read columns of data as strings:
% For more information, see the TEXTSCAN documentation.
formatSpec = '%*s%s%s%s%s%s%s%s%s%s%s%s%s%[^\n\r]';

%% Open the text file.
fileID = fopen(filename,'r');

%% Read columns of data according to format string.
% This call is based on the structure of the file used to generate this
% code. If an error occurs for a different file, try regenerating the code
% from the Import Tool.
dataArray = textscan(fileID, formatSpec, 'Delimiter', delimiter, 'HeaderLines' ,startRow-1, 'ReturnOnError', false);

%% Close the text file.
fclose(fileID);

%% Convert the contents of columns containing numeric strings to numbers.
% Replace non-numeric strings with NaN.
raw = repmat({''},length(dataArray{1}),length(dataArray)-1);
for col=1:length(dataArray)-1
    raw(1:length(dataArray{col}),col) = dataArray{col};
end
numericData = NaN(size(dataArray{1},1),size(dataArray,2));

for col=[2,3,6,10,12]
    % Converts strings in the input cell array to numbers. Replaced non-numeric
    % strings with NaN.
    rawData = dataArray{col};
    for row=1:size(rawData, 1);
        % Create a regular expression to detect and remove non-numeric prefixes and
        % suffixes.
        regexstr = '(?<prefix>.*?)(?<numbers>([-]*(\d+[\,]*)+[\.]{0,1}\d*[eEdD]{0,1}[-+]*\d*[i]{0,1})|([-]*(\d+[\,]*)*[\.]{1,1}\d+[eEdD]{0,1}[-+]*\d*[i]{0,1}))(?<suffix>.*)';
        try
            result = regexp(rawData{row}, regexstr, 'names');
            numbers = result.numbers;
            
            % Detected commas in non-thousand locations.
            invalidThousandsSeparator = false;
            if any(numbers==',');
                thousandsRegExp = '^\d+?(\,\d{3})*\.{0,1}\d*$';
                if isempty(regexp(thousandsRegExp, ',', 'once'));
                    numbers = NaN;
                    invalidThousandsSeparator = true;
                end
            end
            % Convert numeric strings to numbers.
            if ~invalidThousandsSeparator;
                numbers = textscan(strrep(numbers, ',', ''), '%f');
                numericData(row, col) = numbers{1};
                raw{row, col} = numbers{1};
            end
        catch me
        end
    end
end


%% Split data into numeric and cell columns.
rawNumericColumns = raw(:, [2,3,6,10,12]);
rawCellColumns = raw(:, [1,4,5,7,8,9,11]);


%% Replace non-numeric cells with NaN
R = cellfun(@(x) ~isnumeric(x) && ~islogical(x),rawNumericColumns); % Find non-numeric cells
rawNumericColumns(R) = {NaN}; % Replace non-numeric cells

%% Create output variable
ChemBridgePremium50k = table;
ChemBridgePremium50k.MoleculeName = rawCellColumns(:, 1);
ChemBridgePremium50k.SMDC_ID = cell2mat(rawNumericColumns(:, 1));
ChemBridgePremium50k.Lot = cell2mat(rawNumericColumns(:, 2));
ChemBridgePremium50k.Alias = rawCellColumns(:, 2);
ChemBridgePremium50k.Collection = rawCellColumns(:, 3);
ChemBridgePremium50k.Plate = cell2mat(rawNumericColumns(:, 3));
ChemBridgePremium50k.Well = rawCellColumns(:, 4);
ChemBridgePremium50k.Smiles = rawCellColumns(:, 5);
ChemBridgePremium50k.Salt = rawCellColumns(:, 6);
ChemBridgePremium50k.Salt_Count = cell2mat(rawNumericColumns(:, 4));
ChemBridgePremium50k.Solvate = rawCellColumns(:, 7);
ChemBridgePremium50k.Solvate_Count = cell2mat(rawNumericColumns(:, 5));

%% Clear temporary variables
clearvars filename delimiter startRow formatSpec fileID dataArray ans raw col numericData rawData row regexstr result numbers invalidThousandsSeparator thousandsRegExp me rawNumericColumns rawCellColumns R;