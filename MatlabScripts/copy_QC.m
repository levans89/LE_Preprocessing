
main_qc_folder = 'W:\2015_09_HTS_LE\QC';
qc_folder = 'W:\2015_09_HTS_LE\QC\BigScreen\Images\Full';

QC_list = cellstr(num2str([2017018264:1:2017018376]'))
QC_list = cell2table(QC_list);
QC_list.Properties.VariableNames{1} = 'name';
for q=1:height(QC_list)
    source = strcat('W:\2015_09_HTS_LE\plates\','LE_', '20170628', '_InCell2000_plate_',QC_list.name(q),'_10x_t48','\quality_control\');
    destination = strcat(qc_folder);
    if exist (source{1,1},'file');
    copyfile(source{1,1},destination);
    else
        display([QC_list.name(q) 'not found'])
    end
end
for x=1:height(QC_list)
     copyfile(fullfile(main_qc_folder,'QC_template.xlsx'),fullfile(qc_folder,strcat(QC_list.name{x},'.xlsx')));
end