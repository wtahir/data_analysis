import os
import shutil

output_dir = "/home/philipp/output_dir/"
uuid_folder_in_path = 7

with open('test.lst', 'r') as filelist:
    for filepath in filelist:
        uuid_folder = filepath.split('/')[-2]
        new_path_folder = os.path.join(output_dir, uuid_folder)
        try:
            os.makedirs(new_path_folder)
        except FileExistsError:
            print("Error: {} already exists".format(new_path_folder))
        new_path = os.path.join(new_path_folder, "origin.pdf")
        print("\ncopy from {}\ncopy to {}\n".format(filepath.strip(), new_path))
        shutil.copy2(filepath.strip(), new_path)
