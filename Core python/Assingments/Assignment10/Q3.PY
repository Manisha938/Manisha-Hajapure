#Write a program to find the second largest element in the list.
li=[10,20,4,50,60,89,90]
largest=second=li[0]
for i in  li:
    if i >largest:
        second=largest
        largest=i
    elif i > second and i!=largest:
        second=i
print("second largest number is:",second)

