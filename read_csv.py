# csv 'Comma seprated value'

# only use for tabular form :
# Store data in table

# use a csv module
# import reader from it.
# reader function
# use reader or DictWriter

from csv import reader

with open('file.csv','r') as f:
    csv_reader = reader(f)
    # it is a iterator

    # print(type(csv_reader))
    # print(csv_reader)
    for row in csv_reader:
        print(row)
 