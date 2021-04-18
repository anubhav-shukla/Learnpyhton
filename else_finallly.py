# else and finally clause in exeception handlwhile ing
while True:
    try:
     number=int(input('enter a number: '))
    except ValueError:
         print("You didn't entered integer")
    except:
       print('inexepected error !!!')
    else:
      print(f'user input={number}')
      break
    finally:
        print('Finally block...........')



        # Hope now clear else  