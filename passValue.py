def power(x,n):
    ans=1
    for i in range(0,n):
        ans=ans*x
        return(ans)
print(power(12,2))
# python passValue.py

def update(l,i,v):
    if i >= 0 and i<len(l):
        l[i] = v
        return(True)
    else:
        v=v+1
        return(False)
        
        # recursive function
        # 
def factorial(n):
            if n<=0:
                return(1)
            else:
                val=n*factorial(n-1)
                return(val)
print(factorial(10))                

# Find Factor
def factors(n):
    factorlist=[]
    for i in range(1,n+1):
        if n%i ==0:
            factorlist=factorlist+[i]
    return(factorlist)

print(factors(18))
    #check prime 

def isprime(n):
    return(factors(n)==[1,n])

print(isprime(1))    

# list all primes below a given number

def primesupto(n):
    primelist=[]
    for i in range(1,n+1):
        if isprime(i):
            primelist=primelist+[i]
    return(primelist)        

print(primesupto(17))    

# if we need to list first n primes

def nprimes(n):
    (count,i,plist)=(0,1,[])
    while(count < n):
        if isprime(i):
            (count,plist)=(count+1,plist+[i])
        i=i+1 
    return(plist)

print(nprimes(15))         

# why use for :
            # know we scan from 1 to n,use for
# why use while :
            # range to scan not know in advance
#How we use  while to simulate for:
            # for n in rnage(i,j):
            #      statement

            # Now while use :
                    #    n=i
                    # while n<j:
                    #  statement
                    #  n=n+1
#Hope now it is clear

#  for n in l:                  # i=0 
#  statement ------------------>while i<len(l):
                                  #n=l[i]
                                  #statement
                                  #i=i+1

# Hope the next implentaion is clear 

# More about range(i,j) , range(j) , range((#default at 0 )i(start),j(end),k(step)) range(12,1,-3(Difference is 3 and go below)
# ) produce:- 12,9,6,3
# renge (0,len(l)-1)

    #we can use a list to make list using range:
    # type conversion                         list(range(0,5))==[0,1,2,3,4] 
       
# WE understand more about list:
list1=[1,2,3,4]
list2=list1
list1[2]=7
print(list1)
print(list2) # both give same result

# result will be change because both are pointing same list


#  we can make a new list when change without affect first

# same list
list1=[1,2,3,4]
list2=list1
list1=list1[0:2]+[7]+list1[3:]
print(list1)  #here result is different it make a new list
print(list2)


#  How we can extend a  list

list1=[1,2,3,34]
list2=list1
list1.append(12)   # it add new  value  in existing list
print(list1)

        
#  Now if we want to add a  list in list than what 
list1=[1,22,3,34,3]
list2=[1,334,4,3,3,32]
list1.extend(list2) # here you see it add whole list 

print(list1)

# till now we make list manually but now we work 

list1=list(range(10))
print(list1)

list1.append(12)
print(list1)

list1.extend([12,33,44])
print(list1)

list2=list1+list1
print(list2)

list2.remove(5)
list2.remove(5)
print(list2) # now 5 is remove from both  place

# List manipulation
list1=list(range(12))
list1[2:]=[4,3]

print(list1) #you see result in only 4 element it is manipulation

list1[0:2]=[99]
print(list1)

#  List membership

#  we want to remove an elemnt from list 
l=[1,33,2,2,2]
for x in l:
    l.remove(x)
print(l)    
# output 33 , 2
# remove using while

while x in l:
    l.remove(x)
    print(l)  
    # output: 33 
l=[1,33,2,2,2] 
l.reverse()
print(l)   

l.sort()
print(l)

print(l.index(33))

# initialising names
x=1
y=x+1
print(y)