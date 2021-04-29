import os,shutil

# NOTE: You can write every single extension inside tuples
dict_extension={
        'audio_extension' : ('.mp3','.m4a','.wav','.flac'),
        'videos_extension' : ('.mp4','.mkv','.MKV','.flv','.mpeg'),
        'documents_extension' : ('.doc','.pdf','.txt'),
        'image_extension'  : ('.jpg', '.jpeg', '.jpe', '.jif', '.jfif', '.jfi','.png','.gif')
}
folderpath = input('enter folder path')
 
def file_finder(folder_path,file_extension):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files
    # return [file for file in os.listdir(folder_path) for extension in file_extension
    # if file.endswith(extension)]

# print(file_finder(folderpath,video_extensions))
for extension_type, extrension_tuple in dict_extension.items():
    folder_name = extension_type.split('_')[0] + 'Files'
    folder_path = os.path.join(folderpath,folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath,extrension_tuple):
        item_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)
            
    # print('calling file finder')    
    # print(file_finder(folderpath,extrension_tuple))