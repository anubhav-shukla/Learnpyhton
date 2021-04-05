# here we learn about sets comprehension

square={k**2 for  k in range(1,11)}
print(square) #as we know it unordered

# second example:
name=['Anubhav','Mom','Father']
first={n[0] for n in name}
print(first)