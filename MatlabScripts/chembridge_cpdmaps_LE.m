import_chembridge_LE()
ChemBridgePremium50k.Plate = categorical(ChemBridgePremium50k.Plate); % make plates categorical
plates = categories(ChemBridgePremium50k.Plate); % extract list of plates in library

for p = 1:size(plates,1) % for each plate in the list
    
    clear well w thisplate p2 p1 no_extra_sheets n m info cpd_headers cpd_plate c 
    p1 = plates(p,1); % extract platename
    thisplate = ChemBridgePremium50k(ChemBridgePremium50k.Plate == p1(1,1),:); % extract data for that plate
    
    for w = 1:size(thisplate,1) % for each well in the plate
        well.r(w) = strfind('ABCDEFGHIJKLMNOP',thisplate.Well{w}(1,1)); % extract row
        well.c(w) = str2double(thisplate.Well{w}(2:end)); % extract col
    end
    
    well.r = well.r'; % transpose
    well.c = well.c'; % transpose
    
    % move to cell structures to cycle through xlswrite
    no_extra_sheets = 16;
    cpd_plate = cell(no_extra_sheets+1,1);
    
    cpd_headers = {'UsedWells',...%2
        'Cell_Line',...%3
        'Compound_ID',...%4
        'Compound_Category',...%5
        'Dose_Category',...%6
        'Dose',...%7
        'Compound_Usage',...%8
        'MW',...%9
        'Target',...%10
        'Pathway',...%11
        'Description',...%12
        'SALT',...%13
        'SOLVATE',...%14
        'FORM',...%15
        'CAS_Number',...%16
        'SMILES'}';%17
    
    % generate empty templates in plate layout format
    for c = 2:no_extra_sheets+1
        cpd_plate{c,1} = LabelPlateMap_LE();
        cpd_plate{c,1}{1,1}=cpd_headers{c-1,1}; % leave space for info sheet #1
    end
    
    for n = 1:size(thisplate,1) % for each datapoint extracted for thisplate
        cpd_plate{4,1}{well.r(n,1)+1,well.c(n,1)+1} = thisplate.SMDC_ID(n); % assign datapoint to position in structure to become individual sheets
        cpd_plate{17,1}{well.r(n,1)+1,well.c(n,1)+1} = thisplate.Smiles{n};
        cpd_plate{13,1}{well.r(n,1)+1,well.c(n,1)+1} = thisplate.Salt{n};
        cpd_plate{14,1}{well.r(n,1)+1,well.c(n,1)+1} = thisplate.Solvate{n};
        cpd_plate{12,1}{well.r(n,1)+1,well.c(n,1)+1} = thisplate.MoleculeName{n};
        cpd_plate{5,1}{well.r(n,1)+1,well.c(n,1)+1} = 'Unknown';
        cpd_plate{6,1}{well.r(n,1)+1,well.c(n,1)+1} = '1';
        cpd_plate{7,1}{well.r(n,1)+1,well.c(n,1)+1} = '10';
        cpd_plate{8,1}{well.r(n,1)+1,well.c(n,1)+1} = 'query_cpd';
    end
    
    info(1, 1:2) =  {'Dose Format', '10^-3'};
    info(2, 1:2) =  {'Dose', '10'};
    info(3, 1:2) =  {'Dose Category', '1'};
    cpd_plate{1,1} = info;
    
    % write to Excel
    p2 = strcat('0',p1{1,1},'CB-PT04'); % make plate name as barcode format (using plate_database as reference point)
    display(p2)
    xlswrite(['W:\2015_09_HTS_LE\project_database\cpd_plate_keys\ChemBridgeV2\',p2,'.xlsx'],cpd_plate{1,1},'Info'); % rather than write the filename put the entire path
    for m = 2:no_extra_sheets+1
        xlswrite(['W:\2015_09_HTS_LE\project_database\cpd_plate_keys\ChemBridgeV2\',p2,'.xlsx'],cpd_plate{m,1},cpd_plate{m,1}{1,1});
    end
    RemoveSheet123(['W:\2015_09_HTS_LE\project_database\cpd_plate_keys\ChemBridgeV2\',p2,'.xlsx']);  
end

