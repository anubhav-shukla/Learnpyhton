# f=open(file1.txt)
# f.read()
# f.close()

# with block
# context manager

with open ('shukla.txt') as f:
    data =f.read()
    print(data)
# print(f.closed)    