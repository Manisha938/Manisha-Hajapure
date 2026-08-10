#Python Program to Form a New String where the First Character and
#the Last Character have been Exchanged
str1=input("enter a string:")
new_str=str1[-1]+str1[1:-1]+str1[0]

print("new string",new_str)