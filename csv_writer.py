# writer , Dictwriter
from csv import writer
with open('file3.txt','w' ,newline='') as f:
    csv_writer = writer(f)
    # method = writerow,writerows
    csv_writer.writerow(['name','country'])
    csv_writer.writerow(['Anubhav','india'])
    csv_writer.writerow(['Ashish','india'])

    csv_writer. writerows([['name','country'],['Anubhav','india'],['ashish','india']])

    # here we use both method to write a csv file