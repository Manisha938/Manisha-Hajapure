#Write a Python program to find all the unique words and count the
#frequency of occurrence from a given list of strings. Use Python set
#data type.
frist=['Apple','mango','banana','orange','mango','banana']
#unique words
unique=set(frist)

#count frequency
for word in unique:
    count=0
    for i in frist:
        if word==i:
            count=count+1
    print(word,":",count)
    