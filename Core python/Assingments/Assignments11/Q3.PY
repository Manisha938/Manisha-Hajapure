
li=[[5,6],[3,4],[4,8],[2,1]]
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i][1]>li[j][1]:
            temp=li[i]
            li[i]=li[j]
            li[j]=li[temp]
            print("sorted list",li)