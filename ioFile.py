# readfile
# open function
# read method
# seek method
# tell method
# readline method
#readlines=method
#close meth 



# for know cursor position use tell()
# # print(f'cursor position {f.tell()}')  
# # print(f.read())
# print(f.readline()) # print one by one line
# print(f.readline())
# print(f.readline())
# # print(f'cursor position {f.tell()}')
# # # hope now doubt is clear
# # # now see seek method
# # print('before seek method')
# # f.seek(0)
# # print('after seek method')
# # print(f'cursor position {f.tell()}')

# # print(f.read()) # if we read second time than this time our curor at end
# # # this reason it not print .
# readline
# lines= f.readlines()
# for line in lines:
    # print(lines,end='')



# for using different folder file 
# f=open(r"path of file")


 #name , closed
# print(f.closed)


f = open('shukla.txt')
for line in f.readlines()[:2]:
    print(line,end='')
f.close()

