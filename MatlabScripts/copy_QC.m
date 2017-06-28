for q=1:height(QC_list)
    source = strcat('W:\2015_09_HTS_LE\plates\',QC_list(q).name,'\quality_control\');
    destination = strcat(qc_folder);
    copyfile(source,destination);
end

% main_qc_folder = 'W:\2015_09_HTS_LE\QC';
% for x=1:height(QC_list)
%     copyfile(fullfile(main_qc_folder,'QC_template.xlsx'),fullfile(qc_folder,strcat(QC_list.name{x},'.xlsx')));
% end