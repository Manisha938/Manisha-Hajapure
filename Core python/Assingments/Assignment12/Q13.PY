#13. Python Program to count number of digits and letters in a string.
str1= input("enter a string:")
digits=0
letters=0

for ch in str1:
    if(ch >='A' and ch<= 'Z'):
        letters=letters + 1
    elif ch >= '0' and ch <= '9':
        digits=digits + 1

print("number of letters:",letters)
print("number of digits:",digits)
    