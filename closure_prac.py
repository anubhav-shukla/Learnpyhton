# function returing function (Closure) practice

def to_power(x):
    def calc_poower(n):
        return n**x
    return calc_poower 


cube=to_power(3)
print(cube(5))       


square=to_power(2)
print(square(4))


# hope it clear

# start learn decorator from next note