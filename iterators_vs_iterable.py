# iterators vs iterables

numbers=[1,2,3,4] # list,tuple,strings----iterables
squares=map(lambda a:a**2,numbers)#iterator
print(squares) #map object
# for i in numbers:
#     print(i) #here we got result 1
#                                 # 2
#                                 # 3
#                                 # 4
# for i in squares:
#     print(i) #here we got result 1
                                # 4
                                # 9
                                # 16

#Understand working of for loop
# iterable proccessing
number_iter=iter(numbers)
print(next(number_iter))   
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
#print(next(number_iter))     #it give error to stop loop

# hope now iterable is clear
# iter is a object

# now we understand iterator

print(next(squares)) #1
print(next(squares)) #4
print(next(squares)) #9
print(next(squares)) #16
# print(next(squares)) #now it gives error

# iterable work on method
# iterators work on objects

                                   
                                   