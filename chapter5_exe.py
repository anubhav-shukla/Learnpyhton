# take input as list and give output as list square
# python chapter5_exe.py
# inp =input("enter number of elements: ")
# a=list(map(int,input("\n Enter the Numbers: ").strip().split())) 

def square_list(l):
      square = []
      for i in l:
          square.append(i**2)
      return square    
numbers = list(range(1,11))
print(square_list(numbers))