#Python Program to Remove the nth Index Character from a Non-Empty string
str1=input('enter a string:')
n=int(input('enter index to remove:'))

new_str=str1[:n]+str1[n+1]
print('string after removing charachter',new_str)