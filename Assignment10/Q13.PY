# list after removing even number
li=[]
n=int(input('enter the number of elements:'))
for i in range(n):
    num=int(input("enter elements:"))
    li.append(num)

for i in li.copy():
    if i % 2 == 0:
        li.remove(i)

print("list after removing even nubers:",li)
