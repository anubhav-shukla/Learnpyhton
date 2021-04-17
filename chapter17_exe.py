# Exercise .

def divide(a,b):
    try :
         return a/b
    except ZeroDivisionError as err:
        #  print("you can't divide by zero")
        print(err)
    except TypeError as err:
        print('Numbers must be int or float')
    except:
        print('Unexpected error')        
print(divide('4',2))    
