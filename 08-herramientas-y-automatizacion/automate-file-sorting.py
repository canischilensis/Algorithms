import os
import shutil

def sort_files(directory):
    for file in os.listdir(directory):
        ext = file.split('.')[-1]
        folder = os.path.join(directory, ext)
        os.makedirs(folder, exist_ok=True)
        shutil.move(os.path.join(directory, file), os.path.join(folder, file))