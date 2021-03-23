# here we learn how to add two list and items
# python add.py
# cancatenation
fruits=['mango','orange','apple']
fruits1=['banana','grapes']

fruit=fruits+fruits1
# print(fruit)  print all in single list

#  using extend method
# exetnd
fruits.extend(fruits1)
print(fruits)

#  it is doing same work
# append() list in list  [a,[b,c]]
fruits.append(fruits1)
print(fruits)
# insert()
fruits.insert(0,'Apple')
print(fruits)


# thankyou meet  tomarrow with new things