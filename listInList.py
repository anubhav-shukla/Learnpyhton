#  today we check list inside A lsit and print output as input of the list

def checklist_inside(l):
    m=min(l)
    k=max(l)
    n=k-m
    return n
l=[[1,2,3],[4,5,6],[7,8,9]]
print(checklist_inside(l))
