# make a word counter
# python word_counter.py
def word_couter(s):
    count={}
    for char in s:
        
        count[char]=s.count(char)
    return count
print(word_couter('anubhav'))        