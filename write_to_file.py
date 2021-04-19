# use these mode when want change in txt file

# w - only for write
#  a - only insert
#  r+ - read and write both but not create a file

with open('shukla.txt','w') as f:
    f.write("Hello there\n welcome to learning hub")

with open('shukla.txt','a') as f:
    f.write("\nPlease do it")

with open('shukla.txt','r+') as f:
    f.write("Welcome to shukla academy")


    # hope it clear 

