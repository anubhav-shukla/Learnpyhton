# filter odd even
# python filter_odd_even.py
a=list(map(int,input("\n Enter the Numbers: ").strip().split())) 
   
def odd_even_filter(l):
    odd=[]
    even=[]
    for i in l:
      if i%2==0:
        even.append(i)
      else:
        odd.append(i)
    output =[even,odd]
    return output

print(odd_even_filter(a))
