#Write a program of having n number of elements in the list and find out even
#and odd elements in that list and then create two separate lists which will have
#even elements and other will have odd elements.
n=int(input('enter number of elements:'))

frist=[]
even=[]
odd=[]

for i in range(n):
    num=int(input('enter elements:'))
    frist.append(num)

for i in frist:
    if i % 2 == 0:
      even.append(i)
    else:
        odd.append(i)

print("original list:",frist)
print("even list:",even)
print("odd list",odd)