# Renames all files in current folder
import os

path = os.curdir
files = os.listdir(path)


for index, file in enumerate(files):
  if not file == 'renameFiles.py':
    newName = str(index)+ file
    os.rename(os.path.join(path, file), os.path.join(path, newName))