% Louise Evans Feb 2017
% Purpose: replace function of labtoolbox so that batches are quicker to process > create directories.

function set_structures4lines(img_folders, platedata_folder)

for b = 1:length(img_folders)% make all the folders and subfolders for each plate in the project/plates folder
    cd(platedata_folder);
    plate_folder = img_folders{b};
    display(plate_folder)
    
    if ~exist(plate_folder,'dir')
        mkdir(plate_folder)
        cd(plate_folder)
        mkdir('bgs_images')
        mkdir('bgs_images_Alice')
        mkdir('cache')
        mkdir('config')
        mkdir('features\cbfeatures')
        mkdir('features\cbfeatures_Alice')
        mkdir('quality_control')
        mkdir('segmentation')
        mkdir('segmentation_Alice')
    end
end
end