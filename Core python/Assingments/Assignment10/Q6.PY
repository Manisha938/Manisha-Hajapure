#Write a program to remove duplicates from the list.
list=[10,20,30,40,40,50,50,60,70]
new_list=[]
for i in list:
    if i not in new_list:
        new_list.append(i)

print("original list:",list)
print('list after removing duplicates',new_list)