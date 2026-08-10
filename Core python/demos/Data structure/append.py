def createlist(li):
    n=int(input("How many elements you want add:"))

    for i in range(n):
        ele=int(input("enter the element:"))
        li.append(ele)

li=[]
createlist(li)
print(li)