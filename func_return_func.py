# function returning function

def square(a):
    return a**2

def outer_fun():
    def inner_fun():
        print('inside inner func')
    return inner_fun#()

var=outer_fun()
var()    


def ouetr_fun2(msg):
    def inner_fun2():
        print(f"message is {msg}")
    return  inner_fun2
var =ouetr_fun2("Hi shukla")
var()


# till now  we understand some part of predecortator

# hope you understand  func inside a func

