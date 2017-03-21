% Script to remove features files that need to be overwritten or reanalyzed.
% Louise Evans 20.3.2016 Altschuler and Wu Laboratories

% delete path
delete_path = '/Volumes/Project/2015_09_HTS_LE/plates';
%delete_subfolder = 'features/cbfeatures';
delete_subfolder = '\segmentation\';
%delete_subfolder = 'bgs_images';
%delete_subfolder = 'config';

addpath(delete_path);

% list of all plates to choose from
allfiles = dir(delete_path);
allfiles = allfiles(5:end,:);

% plates to delete data from
first = 1;
last = 38;
filestodelete = allfiles(first:last);

% move those files to archive or delete permanently
for i=1:length(filestodelete)
if exist (fullfile(delete_path,filestodelete(i).name,delete_subfolder),'dir')% file finds files or folders, dir finds folders
disp('exist')
movefile(fullfile(delete_path,filestodelete(i).name,delete_subfolder), fullfile(delete_path,filestodelete(i).name,'/archive/'));
%rmdir (fullfile(delete_path,filestodelete(i).name,delete_subfolder),'s')% deletes folder and all subfolders
else
disp ('absent');% display notice if the file is empty
end
end

for i=1:length(filestodelete)
    if ~exist(fullfile(delete_path,filestodelete(i).name,delete_subfolder),'dir')
        disp('no')
        mkdir(fullfile(delete_path,filestodelete(i).name),delete_subfolder)
    else
        disp('exist')
    end
end