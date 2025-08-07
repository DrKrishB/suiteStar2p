import suite2p
import os

def run_suite2p_for_file(tif_file, base_save_path):
    # Extract the file name without extension
    file_name = os.path.splitext(os.path.basename(tif_file))[0]
    
    # Create a unique save path for this file
    save_path = os.path.join(base_save_path, file_name)
    print(save_path)
    ops = {
        #'fast_disk': 'F:\\temp_suite2p',
        'save_path0': save_path,  # Set the save path for this specific file
        'save_mat': 1,
        'reg_tif': 1,
        'reg_tif_chan2': 1,
        'delete_bin': True,
        'nplanes': 1,
        'nchannels': 2,
        'functional_chan': 2,
        'align_by_chan': 2,
        'anatomical_channel': 2,
        'batch_size': 1800,
        'tau': 1.0,
        'fs': 2.0,
        'roidetect': False,
        'sparse_mode': 0,
        'spatial_scale': 0,
        'diameter': 5,
        'connected': True,
        'threshold_scaling': 0.6,
        'max_overlap': 0.5,
        'nbinned': 10000,
        'max_iterations': 30,
        'high_pass': 50.0,
        'allow_overlap': 1,
        'use_cellpose': True,        
        'pretrained_model': 'nuclei',
        'multiplane': False,
        'chan2_thres': 0.3
    }

    db = {
        'look_one_level_down': False,
        'data_path': [folder],
        'tiff_list': [os.path.basename(tif_file)],
        'keep_movie_raw': False
    }

    suite2p.run_s2p(ops=ops, db=db)

# Get folder names with timelapse data
base_directory = os.getcwd()
directory = os.listdir()
fish = sorted([j for j in directory if os.path.isdir(j) and "Zstack" not in j])
print("Available folders:")
for i, folder in enumerate(fish):
    print(f"[{i}] {folder}")

fn_input = input('Enter fish index to analyze (press Enter to run all): ')
if fn_input.strip() == '':
    selected_folders = fish  # run all
else:
    fn = int(fn_input)
    selected_folders = fish[fn:fn+1]  # run just one

# Loop through each selected folder
for folder in selected_folders:
    folder_path = os.path.join(base_directory, folder)
    files = os.listdir(folder_path)
    tif_files = [i for i in files if i.endswith('.tif') and not i.endswith('Preview.tif')]
    ns = len(tif_files)
    print(ns, 'movie files found in', folder)
    for tif_file in tif_files:
        tif_file_path = os.path.join(folder_path, tif_file)
        run_suite2p_for_file(tif_file_path, folder)
