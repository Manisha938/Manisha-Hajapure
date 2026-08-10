#Write a program to create a new list from existing list which contains cube ofeach number of list.
list=[1,2,3,4,5,6,7,8]
cube_list=[]

for i in list:
    cube_list.append(i**3)
print("originial list:",list)
print("cube list:",cube_list)