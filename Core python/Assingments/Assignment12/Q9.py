#9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String
str1=input("enter a string:")
words=str1.split()

word_count=len(words)
char_count=len(str1)

print("number of words:",word_count)
print("number of chacters:",char_count)