function [ cpd_plate ] = generate_cpd_template(no_extra_sheets)
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
    cpd_plate{c,1}{1,1} = cpd_headers{c-1,1}; % leave space for info sheet #1
end


end

