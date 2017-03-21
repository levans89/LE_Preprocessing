#Scripts for facilitating use of Python code

When a new batch is coming in:
- do plate prints of raw images 
	=> script raw_plate_visualization.py (being tested right now)

- compute shading pattern from empty plate or all plates (a warning is not an error, it's just a warning, you can ignore it)
	=> script shading_pattern.py

- create a new plate_params file for this batch
	i. change plate_ids
	ii. change illum_correction_value_file
	(If images have changed size, need to change basicSettings file too)

- create files for launching cluster jobs 
	=> command-line python [...]
- launch cluster jobs
(and possibly repeat for segmentation/feature extraction)