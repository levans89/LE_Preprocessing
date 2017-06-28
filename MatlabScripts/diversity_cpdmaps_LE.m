%% Setup
setpaths()
import_Diversity_LE() % import spreadsheet from supplier
plates96 = categories(categorical(Diversity.Platenum));% derive platenumbers 

p96 = LabelPlateMap96_LE; % template
p384 = LabelPlateMap_LE; % template

c1 = 10; % 10uM concentration
cc1 = 1; % dose cat 1
c2 = 0.03125; % 312.5nM concentration
cc2 = 6; % dose cat 6

% Transfer from 96 to 384 position
cpd_plate96 = [4770;4771;4772;4773;4774;4775;4776;4777;4778;4779;4780;4781;4782;4783;4784;4785;4786;4787;4788;4789];
quadrant = {'Q1';'Q2';'Q3';'Q4';'Q1';'Q2';'Q3';'Q4';'Q1';'Q2';'Q3';'Q4';'Q1';'Q2';'Q3';'Q4';'Q1';'Q2';'Q3';'Q4'};
% c1 plates
cpd_plate384_1={'2017018CPD016';'2017018CPD016';'2017018CPD016';'2017018CPD016';...
                '2017018CPD017';'2017018CPD017';'2017018CPD017';'2017018CPD017';...
                '2017018CPD018';'2017018CPD018';'2017018CPD018';'2017018CPD018';...
                '2017018CPD019';'2017018CPD019';'2017018CPD019';'2017018CPD019';...
                '2017018CPD020';'2017018CPD020';'2017018CPD020';'2017018CPD020'};
% c2 plates
cpd_plate384_2={'2017018CPD021';'2017018CPD021';'2017018CPD021';'2017018CPD021';...
                '2017018CPD022';'2017018CPD022';'2017018CPD022';'2017018CPD022';...
                '2017018CPD023';'2017018CPD023';'2017018CPD023';'2017018CPD023';...
                '2017018CPD024';'2017018CPD024';'2017018CPD024';'2017018CPD024';...
                '2017018CPD025';'2017018CPD025';'2017018CPD025';'2017018CPD025'};

map96to384 = table(cpd_plate96,quadrant,cpd_plate384_1,cpd_plate384_2,'RowNames',plates96); %table of data

% Set structures for plates
diversity1.NSC = cell(5,2);
diversity1.NSC(1,1)= {'2017018CPD016'};
diversity1.NSC(2,1)= {'2017018CPD017'};
diversity1.NSC(3,1)= {'2017018CPD018'};
diversity1.NSC(4,1)= {'2017018CPD019'};
diversity1.NSC(5,1)= {'2017018CPD020'};
for x =1:5
diversity1.NSC{x,2} = p384;
end

diversity1.PubChemID = cell(5,2);
diversity1.PubChemID(1,1)= {'2017018CPD016'};
diversity1.PubChemID(2,1)= {'2017018CPD017'};
diversity1.PubChemID(3,1)= {'2017018CPD018'};
diversity1.PubChemID(4,1)= {'2017018CPD019'};
diversity1.PubChemID(5,1)= {'2017018CPD020'};
for x =1:5
diversity1.PubChemID{x,2} = p384;
end

diversity6.NSC = cell(5,2);
diversity6.NSC(1,1)= {'2017018CPD021'};
diversity6.NSC(2,1)= {'2017018CPD022'};
diversity6.NSC(3,1)= {'2017018CPD012'};
diversity6.NSC(4,1)= {'2017018CPD024'};
diversity6.NSC(5,1)= {'2017018CPD025'};
for x =1:5
diversity6.NSC{x,2} = p384;
end

diversity6.PubChemID = cell(5,2);
diversity6.PubChemID(1,1)= {'2017018CPD021'};
diversity6.PubChemID(2,1)= {'2017018CPD022'};
diversity6.PubChemID(3,1)= {'2017018CPD023'};
diversity6.PubChemID(4,1)= {'2017018CPD02'};
diversity6.PubChemID(5,1)= {'2017018CPD020'};
for x =1:5
diversity6.PubChemID{x,2} = p384;
end

clc
%% Combining 96WP x4 into 384
for p = 1:size(plates96,1)
    plateID_96 = plates96(p,1);
    thisplate = Diversity(Diversity.Platenum == plateID_96,:);
    quadrant = map96to384.quadrant(p,:);
    plateID_384 = map96to384.cpd_plate384_1(p,:);
    pos = find(strcmp(plateID_384,diversity1.NSC(:,1)));
    
    for w = 1:size(thisplate,1) % for each well in the plate
        well.r = strfind('ABCDEFGH',thisplate.WellID{w}(1,1)); % extract row 
        well.c = str2double(thisplate.WellID{w}(2:end)); % extract col 
        if strcmp(quadrant,'Q1')==1
            well.r = (2*well.r)-1+1;% shift for map and pipetting 96to384
            well.c = (2*well.c)-1+1;
        elseif strcmp(quadrant,'Q2')==1
            well.r = (2*well.r)-1+1;
            well.c = (2*well.c)+1;
        elseif strcmp(quadrant,'Q3')==1
            well.r = (2*well.r)+1;
            well.c = (2*well.c)-1+1;
        elseif strcmp(quadrant,'Q4')==1
            well.r = (2*well.r)+1;
            well.c = (2*well.c)+1;
        end
        diversity1.PubChemID{pos,2}{well.r,well.c} = thisplate.PubChemID(w);
        diversity1.NSC{pos,2}{well.r,well.c} = thisplate.NSC(w);
    end
    clear PubChemID NSC pos prepos p p1 w
end

%% move to cell structures to cycle through xlswrite
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
    cpd_plate{c,1}{1,1} = cpd_headers{c-1,1}; % leave space for info sheet #1
end

for n = 1:size(diversity_pubchem,1) % for each datapoint extracted for thisplate

end

info(1, 1:2) =  {'Dose Format', '10^-3'};
cpd_plate{1,1} = info;

info(2, 1:2) =  {'Dose', c1};
info(3, 1:2) =  {'Dose Category', cc1};

for p = 1:5
cpd_plate{4,1} = diversity_NSC(p,2); % assign datapoint to position in structure to become individual sheets
cpd_plate{12,1} = diversity_PubChemID(p,2);
end

% write to Excel
xlswrite(['W:\2015_09_HTS_LE\project_database\cpd_plate_keys\AW_Libraries\',p2,'.xlsx'],cpd_plate{1,1},'Info'); % rather than write the filename put the entire path
for m = 2:no_extra_sheets+1
    xlswrite(['W:\2015_09_HTS_LE\project_database\cpd_plate_keys\AW_Libraries\',p2,'.xlsx'],cpd_plate{m,1},cpd_plate{m,1}{1,1});
end
RemoveSheet123(['W:\2015_09_HTS_LE\project_database\cpd_plate_keys\AW_Libraries\',p2,'.xlsx']);



