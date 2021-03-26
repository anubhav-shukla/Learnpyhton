#  today we check list inside A lsit and print output as input of the list
# python Lst.py
def checklist_inside(l):
    count =0
    for i in l:
        if type(i) == list:
            count+=1
    return count
b=[1,2,3,[4,5,6],[7,8,9]]
print(checklist_inside(b))
