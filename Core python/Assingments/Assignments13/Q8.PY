#8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary
s=input('enter a string:')

#split the string into words
words=s.split()

d={}

for word in words:
    if words in d:
        d[word]=d[word]+1
    else:
        d[word]=1
print("words frequency")
print(d)
