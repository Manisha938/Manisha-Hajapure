
li=["apple","kiwi","banana","orange","mango","mango","banana"]
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if len(li[i])>len(li[j]):
            temp=li[i]
            li[i]=li[j]
            li[j]=temp
print("sorted list:",li)
      