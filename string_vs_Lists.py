# list vs strings

# strings are immutable 
# lists are mutable

# python string_vs_Lists.py
s="string" 
s.title()#you can't change it
t=s.title() #here we make new string and now result is different
# hope immutable is clear
print(t)

#  now see lists

l =['word','apple','word3']
l.append('word3')
print(l)