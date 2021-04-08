# This is challenge with practice

# define a function take any no of list contaning number
# [1,2,3],[4,5,6],[7,8,9]
# return average
# (1+4+7)/3,(2,5,8)/3,(3,6,9)/3


# try to make this anobymous function in one line using lambda expression

# def average_finder(*args):
#     average=[]
#     for pair in zip(*args):
#        average.append( sum(pair)/len(pair))
#     return average
# print(average_finder([1,2,3],[4,5,6],[7,8,9]))


# Now we use lambda expression

short =lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
print(short([1,2,3],[4,5,6],[7,8,9]))

# Hope it clear
