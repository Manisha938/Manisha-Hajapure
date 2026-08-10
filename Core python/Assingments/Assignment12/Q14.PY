#14. Python Program to count the occurrences of ach word in a string.
str1=input("enter  a string:")
words=str1 .split()
for i in range(len(words)):
    count=1
    if words[i] != " ":
        for j in range(i+1,len(words)):
            if words[i] ==words[j]:
                count =count + 1
                words[j]=" "

        print(words[i],"=",count)



