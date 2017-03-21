% Louise Evans

function [] = flipdata_LE(original_path, output_path) 
    img_ext = 'tif';
    img_list = dir(fullfile(original_path,['*.' img_ext]));
    if isempty(img_list)
    return
    end
    % use folder name as file prefix
    [~,base_name] = fileparts(original_path);
    base_name = strrep(base_name,'.','_');

    for i = 1:length(img_list)
        % 1. get row
        ROW = img_list(i).name(1);

        % 2. get column
        COL = regexpi(img_list(i).name,'-\s(\d+)','tokens');
        COL = COL{1}{1};

        % 3. get frame
        Frame = regexpi(img_list(i).name,'fld\s(\d)\swv','tokens');
        Frame = sprintf('%04s',Frame{1}{1}); 

        % 4. get channel
        WV = regexpi(img_list(i).name,'wv\s(\w+)\s-','tokens');
        WV = WV{1}{1};
    
        switch WV
            case 'CFP'
                ch = '1';

            case 'TexasRed'
                ch = '3';

            case 'YFP'
                ch = '2';

            otherwise
                error('Unknown fluorescence.')
        end
        
        switch ROW
            case 'A'
                row = 'P';
            case 'B'
                row = 'O';
            case 'C'
                row = 'N';
            case 'D'
                row = 'M';
            case 'E'
                row = 'L';
            case 'F'
                row = 'K';
            case 'G'
                row = 'J';
            case 'H'
                row = 'I';
            case 'I'
                row = 'H';
            case 'J'
                row = 'G';
            case 'K'
                row = 'F';
            case 'L'
                row = 'E';
            case 'M'
                row = 'D';
            case 'N'
                row = 'C';
            case 'O'
                row = 'B';    
            case 'P'
                row = 'A';
            otherwise 
                error ('unknown')
        end
        
        switch COL
            case '24'
                col = '1';
            case '23'
                col = '2';
            case '22'
                col = '3';
            case '21'
                col = '4';
            case '20'
                col = '5';
            case '19'
                col = '6';
            case '18'
                col = '7';
            case '17'
                col = '8';
            case '16'
                col = '9';
            case '15'
                col = '10';
            case '14'
                col = '11';
            case '13'
                col = '12';            
            case '12'
                col = '13';
            case '11'
                col = '14';
            case '10'
                col = '15';
            case '9'
                col = '16';
            case '8'
                col = '17';
            case '7'
                col = '18';
            case '6'
                col = '19';
            case '5'
                col = '20';       
            case '4'
                col = '21';
            case '3'
                col = '22';
            case '2'
                col = '23';
            case '1'
                col = '24';
        end
     
        % 5. make the new file name
    %     new_name = [base_name '_' [ROW COL] '_' WV '_' Frame '-' ch '.' img_ext];
        new_name = [base_name '_' row col '_' Frame '-' ch '.' img_ext];

        % 6. create the well folde if it does not exist
        well_folder = fullfile(output_path,[row col]);
        if ~exist(well_folder,'dir')
            mkdir(well_folder)
        end

        % 7. copy the file and rename it
        copyfile(fullfile(original_path,img_list(i).name),...
            fullfile(well_folder,new_name));  
    end
    end
