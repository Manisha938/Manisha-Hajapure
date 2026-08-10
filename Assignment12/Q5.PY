#Python Program to Count the Number of Vowels in a String
s=input("enter a string:")
count=0

for ch in s:
    if ch in "aeiou":
        count=count + 1

print("number of vowel=",count)