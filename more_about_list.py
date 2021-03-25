# generate lists with range function
# something more about pop method
# index method
# pass list to a function

# python more_about_list.py
numbers=list(range(1,11))
# print(numbers)
# how to know what value are pop()
print(numbers.pop()) #see result is 10 that is pop()
# print(numbers) # 10 is removed from list
# print(numbers.index(1,11,14) # it show position of element
# index(value,start, end)
def negative_list(l):
    negative = []
    for  i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers))        
  
