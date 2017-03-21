% Louise Evans March 2017
function exp_anno_maker4lines(currexp, cpd_DB, year, expt)

%create info page
info(1, 1:2) =  {'Project Name', '2015_09_HTS_LE'};
info(2, 1:2) =  {'Owner', 'levans'};
info(3, 1:2) =  {'Year', year};
info(4,1:2) = {'Batch', expt};
info(5, 1:2) =  {'Number of Wells', 384};
info(6, 1) = {'Physical Plate ID'};
info(7, 1) =  {'Cell Lines'};

info(8, 1:2) =  {'Number of Sheets', 16};
info(9, 1:1) =  {'Sheet Fields'};
info(9, 2:17) = {'UsedWells' 'Cell_Line' 'Compound_ID' 'Compound_Category' 'Dose_Category' 'Dose' 'Compound_Usage' 'MW' 'Target' 'Pathway' 'Description' 'SALT' 'SOLVATE' 'CAS_Number' 'Form' 'SMILES' };
info(10, 1:2) = {'Markers Sets','pSeg (CFP/mCherry),YFP'};
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
for k = 51:size(currexp,1)
    try
        info{6,2}= currexp.expt_plate{k};
        disp(num2str(currexp.expt_plate{k}))
        info{7,2}= currexp.CellLine{k}
        info{11,2} = currexp.plate_type{k}
        
        info{12,2}= currexp.cpd_plate_1{k}
        info{13,2}= currexp.cpd_plate_1_dilution{k}
        
        info{15,2}= currexp.cpd_plate_2{k}
        info{16,2}= currexp.cpd_plate_2_dilution{k}
        
        info{18,2}= currexp.cpd_plate_PC{k}
        info{19,2}= currexp.cpd_plate_PC_dilution{k}
        
        
        
        %find the associated perturbation plates in the plate database
        APCP_name = {currexp.cpd_plate_1{k}, currexp.cpd_plate_2{k},currexp.cpd_plate_PC{k}};
        
        [~,APCP_pos] = ismember(APCP_name, cpd_DB.PlateBarcode);
        no_extra_sheets = 16;%minus row header
        APCP_pos = APCP_pos'
        for c = 1:3
            library{c,1} = table2cell(cpd_DB(APCP_pos(c),{'Library'}));   %col number where library is
            library_path{c,1} = fullfile('W:\2015_09_HTS_LE\project_database\cpd_plate_keys\',library{c,1});
        end
        
        
        
        
        APCP =cell(no_extra_sheets+1,size(library_path,1));
        for j=1:size(library_path,1)
            cd (library_path{j,1}{1,1})
            [~,~,APCP{1,j}] = xlsread(strcat(APCP_name{j},'.xlsx'),1,'A1:B3');
            for i = 2:no_extra_sheets+1
                [~,~,APCP{i,j}] = xlsread(strcat(APCP_name{j},'.xlsx'),i); %get rid of CD and use fullfile to point to full path
            end
        end
        
        info{14,2}= APCP{1,1}{1,2}
        info{17,2}= APCP{1,2}{1,2}
        info{20,2}= APCP{1,3}{1,2}
        
        % division and multiplication of doses depending on protocol
        %APCP{5,1}(2:17,2:25)= num2cell(cell2mat(APCP{5,1}(2:17,2:25))/str2double(info{14,2}));
        %APCP{5,2}(2:17,2:25)= num2cell(cell2mat(APCP{5,2}(2:17,2:25))/str2double(info{17,2}));
        %APCP{5,3}(2:17,2:25)= num2cell(cell2mat(APCP{5,3}(2:17,2:25))/str2double(info{20,2}));
        
        for i=4:size(APCP,1) % first sheets are info usedwells cellline
            for j=1:size(APCP,2)
                for y = 1:17
                    for z = 1:25
                        APCP{i,j}{y,z} = num2str(APCP{i,j}{y,z});
                        if strcmp(APCP{i,j}{y,z},'NaN');
                            APCP{i,j}{y,z}=[];
                        end
                    end
                end
            end
        end
        
        for i=2:3
            for j=1:3
                APCP{i,j}=map;
            end
        end
        
        exp_plate = cell(no_extra_sheets+1,1);
        exp_plate{1}=info;
        for v = 2:length(exp_plate)
            exp_plate{v} = map;
        end;
        
        for i=2:size(APCP,1)
            for x=2:17;
                for y=2:25;
                    thiswell = horzcat(APCP{i,1}(x,y),APCP{i,2}(x,y), APCP{i,3}(x,y));
                    uniwell = find(~cellfun(@isempty, thiswell));
                    if (length(uniwell)>1)
                        error('Multiple values in same position');
                    else
                        try
                            exp_plate{i}{x,y} = thiswell{uniwell};
                            if  i == 2 % just picked 2 out of 6 sheets
                                exp_plate{7}{x,y} = info{7,2};
                                exp_plate{2}{x,y} = 1;
                            end
                        catch
                            %warning('oops');
                        end
                    end
                end
            end
        end
        
        
        for m = 2:no_extra_sheets+1;
            exp_plate{m,1}(1, 1)= info(9,m);
        end
        
        % add cellline data and fill with usedwells info
        for x=2:17
            for y=2:25
                exp_plate{3}{x,y}=currexp.CellLine{k}
                exp_plate{2}{x,y}=[1]
            end
        end
        
        xlswrite(['W:\2015_09_HTS_LE\project_database\expt_plate_keys\',num2str(currexp.expt_plate{k}),'.xlsx'],exp_plate{1,1},'Info'); % rather than write the filename put the entire path
        for m = 2:no_extra_sheets+1
            xlswrite(['W:\2015_09_HTS_LE\project_database\expt_plate_keys\',num2str(currexp.expt_plate{k}),'.xlsx'],exp_plate{m,1},exp_plate{m,1}{1,1});
        end
        disp(currexp.expt_plate{k})
        RemoveSheet123(['W:\2015_09_HTS_LE\project_database\expt_plate_keys\',num2str(currexp.expt_plate{k}),'.xlsx']);
    end
end

