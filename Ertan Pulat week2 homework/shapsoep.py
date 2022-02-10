word_1 = input("Enter a word1:")
for i in word_1:
    x = tuple(word_1)    
word_2 = input("Enter a word2:")
for k in word_2:
    y = tuple(word_1)
    break
x = set(x)
y= set(y)
list = [sorted(x&y),sorted(x-y),sorted(y-x)]
print(list)
