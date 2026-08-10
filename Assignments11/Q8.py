li=[]
for i in range(1,101):
    li.append(i)

for i in range(9,-1,-1):
    if i % 2 == 0:
        for j in range(i*10,i*10+10):
            print(li[j],end="\t")
        else:
            for j in range(i * 10+9,i*10 -1,-1):
                print(li[j],end="\t")
#print()

         
