import time
# list vs  generator
# memory usage , time
# when to use list , when to use generator
# list
t1=time.time()
l=[i**2 for i in range(10000000)] #10 million #it uses near 400 mb
print(f"{time.time()-t1} second")

# generator
t2=time.time()
g = (i**2 for i in range(10000000)) #10 million #too less time
print(f"{time.time()-t2} second")


# see the differnce

# hope it  clear

