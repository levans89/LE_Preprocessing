% Louise Evans March 2016
function exp_anno_maker(batch, plate_DB_path,plate_DB, year)

%Code
[~, ~, Exp_DB] = xlsread(fullfile(plate_DB_path,plate_DB),1);
[~,~,Cpd_DB] = xlsread(fullfile(plate_DB_path,plate_DB),2);
pos = find(strcmp(Exp_DB(:,2),batch));

%create info page
info(1, 1:2) =  {'Project Name', '2015_09_HTS_LE'};
info(2, 1:2) =  {'Owner', 'levans'};
info(3, 1:2) =  {'Year', year};
info(4,1:2) = {'Batch', batch};
info(5, 1:2) =  {'Number of Wells', 384};
info(6, 1) = {'Physical Plate ID'};
info(7, 1) =  {'Cell Lines'};

info(8, 1:2) =  {'Number of Sheets', 16};
info(9, 1:1) =  {'Sheet Fields'};
info(9, 2:17) = {'UsedWells' 'Cell_Line'	'Compound_ID'	'Compound_Category' 'Dose_Category'	'Dose'	'Compound_Usage' 'MW' 'Target'	'Pathway'	'Description' 'SALT' 'SOLVATE' 'FORM' 'CAS_Number' 'SMILES'};
info(10, 1:2) = {'Markers Sets','pSeg (CFP/mCherry),YFP-XRCC5'};
info(11, 1) =  {'plate_type'};
info(12, 1) =  {'Associated Perturbation plate 1'};
info(13, 1) = {'APP1 Dilution'};
info(14, 1:2) = {'APP1 Dose Format','10^-3'};
info(15, 1) = {'Associated Perturbation plate 2'};
info(16, 1) = {'APP2 Dilution'};
info(17, 1:2) = {'APP2 Dose Format','10^-3'};
info(18, 1) = {'Associated Positive Control Plate'};
info(19, 1) = {'APCP Dilution'};
info(20, 1:2) = {'APCP Dose Format','10^-3'};
info(21, 1:2) = {'Number of Rows', 16};
info(22, 1:2) = {'Number of Columns',24};

%create map for other sheets
map(2:17,1) = cellstr(('A':'P')')';
map(1,2:25) = num2cell(1:24);

%find position of the experiment plate in the plate database
for k = pos(1):pos(end)
    
    info{6,2}= Exp_DB{k,5};
    disp(num2str(Exp_DB{k,5}))
    info{7,2}= Exp_DB{k,6};
    info{11,2} = Exp_DB{k,8};
    info{12,2}= Exp_DB{k,15};
    info{13,2}= Exp_DB{k,16};
    info{15,2}= Exp_DB{k,17};
    info{16,2}= Exp_DB{k,18};
    info{18,2}= Exp_DB{k,19};
    info{19,2}= Exp_DB{k,20};

    %find the associated perturbation plates in the plate database
    APCP_name = {Exp_DB{k,15}, Exp_DB{k,17},Exp_DB{k,19}};
    [~,APCP_pos] = ismember(APCP_name, Cpd_DB(:,1));
    no_extra_sheets = (size(info,2)-1);%minus row header
    library = Cpd_DB(APCP_pos,3);   %col number where library is
    library_path = fullfile('W:\2015_09_HTS_LE\project_database\cpd_plate_keys\',library);
    APCP = cell(no_extra_sheets+1,size(library_path,1));
    
    for j = 1:size(library_path,1)
        cd (library_path{j,1})
        [~,~,APCP{1,j}] = xlsread(strcat(APCP_name{j},'.xlsx'),1,'A1:B3');
        for i = 2:no_extra_sheets+1
            [~,~,APCP{i,j}] = xlsread(strcat(APCP_name{j},'.xlsx'),i);
        end
    end
    
    info{14,2} = APCP{1,1}{1,2};
    info{17,2} = APCP{1,2}{1,2};
    info{20,2} = APCP{1,3}{1,2};
    
    % division and multiplication of doses depending on protocol
    APCP{7,1}(2:17,2:25)= num2cell(cell2mat(APCP{7,1}(2:17,2:25))/str2double(info{14,2}));
    APCP{7,2}(2:17,2:25)= num2cell(cell2mat(APCP{7,2}(2:17,2:25))/str2double(info{17,2}));
    APCP{7,3}(2:17,2:25)= num2cell(cell2mat(APCP{7,3}(2:17,2:25))/str2double(info{20,2}));
    
    for i=2:size(APCP,1)
        for j=1:size(APCP,2)
            for y = 1:17
                for z = 1:25
                    APCP{i,j}{y,z} = num2str(APCP{i,j}{y,z});
                    if strcmp(APCP{i,j}{y,z},'NaN')
                        APCP{i,j}{y,z}=[];
                    end
                end
            end
        end
    end
    
    exp_plate = cell(no_extra_sheets+1,1);
    exp_plate{1}=info;
    for v = 2:length(exp_plate)
        exp_plate{v} = map;
    end;
    
    for i = 2:length(APCP)
        for x = 2:17
            for y = 2:25
                thiswell = horzcat(APCP{i,1}(x,y),APCP{i,2}(x,y), APCP{i,3}(x,y));
                uniwell = find(~cellfun(@isempty, thiswell));
                if (length(uniwell)>1)
                    error('Multiple values in same position');
                else
                    try
                        exp_plate{i}{x,y} = thiswell{uniwell};% plus one to shift it along one to allow to add in the usedwells after
                    catch
                        %warning('oops');
                    end
                    if  i == 2 % just picked 2 out of 6 sheets
                        exp_plate{3}{x,y} = info{7,2};
                        exp_plate{2}{x,y} = 1;
                    end
                end
            end
        end
    end
    
    for m = 2:no_extra_sheets+1
        exp_plate{m,1}(1, 1) = info(9,m);
    end

    xlswrite(['W:\2015_09_HTS_LE\project_database\expt_plate_keys\',num2str(Exp_DB{k,5}),'.xlsx'],exp_plate{1,1},'Info'); % rather than write the filename put the entire path
    for m = 2:no_extra_sheets+1
        xlswrite(['W:\2015_09_HTS_LE\project_database\expt_plate_keys\',num2str(Exp_DB{k,5}),'.xlsx'],exp_plate{m,1},exp_plate{m,1}{1,1});   
    end
    
    RemoveSheet123(['W:\2015_09_HTS_LE\project_database\expt_plate_keys\',num2str(Exp_DB{k,5}),'.xlsx']);
end
end

