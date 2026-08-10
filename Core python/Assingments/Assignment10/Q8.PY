#Write a program to create a duplicate of an existing list. It should not point to same list.
li1=[10,20,30,30,40,50,50,60,60,70,80]
li2=li1.copy()
print("original list:",li1)
print("duplicate list:",li2)