function makeQCfiles_LE(batch,plate_DB_path,plate_DB)
% Louise Heinrich 2017.05.12 in Altschuler & Wu Laboratories
[~, ~, Exp_DB] = xlsread(fullfile(plate_DB_path,plate_DB),1);
headers = Exp_DB(1,:);
Exp_DB = cell2table(Exp_DB);
Exp_DB.Properties.VariableNames = headers;
Exp_DB(1,:) = [];
main_qc_folder = 'W:\2015_09_HTS_LE\QC';
currexp = Exp_DB(strcmp(Exp_DB.batch,batch{1,1}),:);
for x=1:size(currexp,1)
    copyfile(fullfile(main_qc_folder,'QC_template.xlsx'),fullfile(main_qc_folder,'bigscreen',strcat(currexp.expt_plate{x},'.xlsx')));
end
end
