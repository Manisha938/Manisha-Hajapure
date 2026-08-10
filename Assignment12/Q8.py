#8. Python Program to Remove the Characters of Odd Index Values in String
str1=input("enter a string:")
new_str=" "
for i in range(len(str1)):
    if i % 2 ==0:
        new_str=new_str + str1[i]
print("string after removing odd index character:",new_str)
