#
#li=[i for i in range(1,11)]
#print(li)
#sqr=[i**2 for i in li]
#print(sqr)
#s="firstbit"
#res=[i.upper()for i in s]
#print(res)

#li=["I","Am","Good","In","python"]
#li=[]
#for i in range(1,101):
    #if i %2!=0:
        #li.append(i)
#print(li)
#li[i]
  
#for i in range(1,11):
    #if i  % 2 ==0:
       # print(i)
    #else:
       # print(i)
#li=["even"if i% 2==0 else"odd"for i in range(1,11)]
#print(li)

dic={i:i* i for i in range(1,20)}
for i in range(1,20):
    dic[i]=i**i
print(dic)
