#3. Python Program to Detect if Two Strings are Anagrams
str1=input("enter frist string:")
str2=input("enter second string:")

if sorted(str1) == sorted(str2):
    print("string are anagrams:")
else:
    print("string are not anagram:")