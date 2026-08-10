#9. Write a Python program to find all the unique combinations of 3

frist=[1,2,3,4,5,6,7,8]
#target sum
target=int(input("enter  target sum:"))

#find conbination
for i in range(len(frist)):
    for j in range(i + 1,len(frist)):
        for k in range(j+1,len(frist)):
            if frist(i) + frist [j]+ [k]== target:
                print(frist[i],frist[j],frist[k])