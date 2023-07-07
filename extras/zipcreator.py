import zipfile
import pathlib

def compress(files,folder):
    folder_dir = pathlib.Path(folder,'compressed.zip')
    with zipfile.ZipFile(folder_dir,'w') as file:
        for file_path in files:
            file_path = pathlib.Path(file_path)
            file.write(file_path, arcname=file_path.name)
