import os
import shutil
from getch import pause

print('Welcome to Flacks File Sorter App')
path = input('Enter directory: ')
files = os.listdir(path)

for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)


print('All files have been sorted!')
pause("Press Any Key To Exit.")