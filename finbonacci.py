# here  we write  a  program for fibonacci series

def fibonacci_seq(n):
    a=0
    b=1
    if n==1:
        print (a)
    elif n==2:
        print(b)
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c=a+b #c==1
            a=b #a==1
            b=c #b==1  It is called swapping
            print(b,end=" ")

fibonacci_seq(10)


# python finbonacci.py

# python fibonacci_.py

