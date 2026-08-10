#Write a program to remove all occurrences of a given element in the list.
n=int(input("enter number of elements:"))
frist=[]
for i in range(n):
    num=int(input('enter elements:'))
    frist.append(num)
x=int(input('enter elements to remove'))
new_list=[]
 
for i in frist:
    if i!= x:
        new_list.append(i)

print("original list:",frist)
print("list after removing element:",new_list)
