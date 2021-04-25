import os
import shutil
# os.chdir(r'D:\Python hh\os_module')
# # print(os.listdir())
# fileiter=os.walk(r'D:\Python hh\os_module')
# for current_path,folder_names,file_names in fileiter:
#     print(f'current path : {current_path}')
#     print(f'folder names: {folder_names}')
#     print(f'file names : {file_names}')

    # how can we delete a folder

    # os.rmdir('movies')
    # folder inside a folder by one command
# os.makedirs('new/movies')
# shutil.rmtree('movies')
    # but keep in mind :
        #    it delete permanently deleted file not in recycle bin
# shutil.copytree('movies', 'chapter20\movie')

# shutil.copy('file.txt','chapter20/file.txt')

# shutil.move('file.txt','movies/file2.txt') #for file move
shutil.move('movies','movie/new2') #for move a  complete folder


