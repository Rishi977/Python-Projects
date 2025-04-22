#Importing essential Libraries

import os   # Os is useful to interact with operating system to perform some tasks.


folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "test_folder")


for filename in os.listdir(folder_path):
    if filename.endswith(".rtf"):
        old_path = os.path.join(folder_path, filename)
        new_filename = "new_" + filename
        new_path = os.path.join(folder_path, new_filename)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")
