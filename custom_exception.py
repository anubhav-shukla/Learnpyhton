# python cudtom exeception
# Q- why custom execeptions?
#  A-to read readability of code

# example

# def validate(name):
#     if (len)<8:
#         raise ValueError('name is too short')
# username=input('Enter tyour name: ')
# validate(username)
# print(f'Hello {username}')        


class NameTooShortErr(ValueError):
    pass
def validate(name):
    if len(name)<8:
        raise NameTooShortErr('name is too short')
username=input('Enter tyour name: ')

validate(username)
print(f'Hello {username}')        



# hope you now able too create to error