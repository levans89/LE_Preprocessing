% Louise Evans
%import file
map_source = 'W:\2015_09_HTS_LE\LE_project_database\drug_libraries\AW SMDC Drug Libraries Raw Data';
cd(map_source)
map_name = 'CalBiochem_Kinase_Inhibitor_2012.xls'
[raw txt num] = xlsread(map_name)

%extract matlab-readable relevant data to structure
map.Well=txt(3:386,2);
map.Cat_No=num(3:386,3);
map.Compound_ID=num(3:386,4); 
map.CAS_Number=num(3:386,5);
map.MW=num(3:386,6);
map.Dose=num(3:386,7);
map.Purity=num(3:386,8);
map.Permeablilty=num(3:386,9);
map.ATP_Comp=num(3:386,10);
map.Reversibility=num(3:386,11);
map.IC50=num(3:386,13);
map.PubChem_Cpd_ID=num(3:386,15);
map.Pathway=num(3:386,16);

%remove NaNs
platestructs = {map.Well,...
                map.Cat_No,...
                map.Compound_ID,...
                map.CAS_Number,...
                map.MW,...
                map.Dose,...
                map.Purity,...
                map.Permeablilty,...
                map.ATP_Comp,...
                map.Reversibility,...
                map.IC50,...
                map.PubChem_Cpd_ID,...
                map.Pathway}'
            platestructs_names = {'Well',...
                'Cat_No',...
                'Compound_ID',...
                'CAS_Number',...
                'MW',...
                'Dose',...
                'Purity',...
                'Permeablilty',...
                'ATP_Comp',...
                'Reversibility',...
                'IC50',...
                'PubChem_Cpd_ID',...
                'Pathway',...
                'Dose_Category'}'

for j = 1:size(platestructs,1)
    NAN = cellfun(@isnan,platestructs{j,1},'UniformOutput', false);
    for i = 1:384
        if NAN{i}==1
            platestructs{j,1}{i}=[];
        end
    end
end

map.Well= platestructs{1,1};
map.Cat_No= platestructs{1,1};
map.Compound_ID= platestructs{3,1};
map.CAS_Number= platestructs{4,1};
map.MW= platestructs{5,1};
map.Dose= platestructs{6,1};
map.Purity= platestructs{7,1};
map.Permeablilty= platestructs{8,1};
map.ATP_Comp= platestructs{9,1};
map.Reversibility= platestructs{10,1};
map.IC50= platestructs{11,1};
map.PubChem_Cpd_ID= platestructs{12,1};
map.Pathway= platestructs{13,1};

%index Cpd and assign dose category
map.Dose_Category = num(3:386,7);
NAN = cellfun(@isnan,map.Dose_Category,'UniformOutput', false);
for i=1:384
    if NAN{i}==0
        map.Dose_Category{i}=[1];
    else
        if NAN{i}==1
            map.Dose_Category{i}=[];
        end
    end
end
platestructs{14,1}=map.Dose_Category;

% define location of each well
for i=1:384
map.Well{i,1}
well.r(i) = strfind('ABCDEFGHIJKLMNOPQ',map.Well{i,1}(1));% you only want the first character of the well name
well.c(i) = str2num(map.Well{i,1}(2:end));
end
well.r=well.r'
well.c=well.c'

%convert vectors to matrix for each map.
for z = 1:size(platestructs,1)
    [template] = LabelPlateMap_LE()
    for k=1:384
        template{well.r(k,1)+1,well.c(k,1)+1} = platestructs{z,1}{k,1}
    end
    platestructs{z,1}=template;
    platestructs{z,1}{1,1} = platestructs_names{z,1}
end

% write combinded file to Excel sheet in same folder as you got the files
% from
for y=1:size(platestructs,1)
xlswrite('2016018CPD010.xlsx',platestructs{y,1},y)
end





% Label Plate Map
function [template] = LabelPlateMap_LE()
rows = 'ABCDEFGHIJKLMNOP';
template = cell(17, 25);
for i = 2:17
    template (i, 1) = {rows(i-1)};
end
for i = 2:25
    template(1, i) = {num2str(i-1)};
end
end