# decorators - enhance the functionality of other function
# @ use for decorator

def decorator_f(any):
    def wrapper_f():
       print('this is awesome function')
       any()
    return wrapper_f
    # this is aawesome function
@decorator_f  #shortcut it is called syntactic 
def func():
    print('This is function 1')
func()
def func2():
    print('This is function 2')

# Now we use decorator

var=decorator_f(func2)

var()


