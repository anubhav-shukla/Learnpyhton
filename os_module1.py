import os
# os.getcwd()
# os.chdir(r'D:\Python hh\os_module')
# print(os.getcwd())

# os.mkdir('movies')
# print(os.path.exists('movies'))

# if os.path.exists('movies'):
#     print('already exists')
# else:
#     os.mkdir('movies')    

# open('file.txt','a').close()
# it gives error  

# os.mkdir('D:\Python hh\os_module\movies')
# print(os.listdir())
# print(os.listdir(r'D:\Python hh\os_module'))

for item in os.listdir():
    path =  os.path.join(os.getcwd(),item)
    print(path)

for item in os.listdir(r'D:\Python hh\os_module'):
    path =  os.path.join(r'D:\Python hh\os_module',item)
    print(path)
