
list1=[1,2,3,4,5]
list2=[3,4,5,6]

intersection=[]

for i in list1:
    if i in list2:
        intersection.append(i)
print("intersection list:", intersection)
