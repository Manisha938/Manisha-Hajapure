#12. Python Program to count number of lowercase characters in a string.
str1=input("enter a string:")
count=0

for ch in str1:
    if ch >='a' and ch <='z':
        count=count+1

print("number of lowercase character:",count)
