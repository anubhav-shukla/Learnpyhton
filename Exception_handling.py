# Exception handling
# try except else finally

# Exception are those error who comes during execution
while True:
    try:
        age=int(input('enter your age: '))#seven
        break
    except ValueError: 
        print('Maybe you entered string instead of number , try again')
    except:
        print('Unexpected error')


if age <18:
    print('you can\'t play this game')
else:
    print('You can play this game')    