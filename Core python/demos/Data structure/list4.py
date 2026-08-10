li=[34,56,78,90,57,98,48,890]

max=li[0]
for i in range(1,len(li)):
    if(li[i]> max):
        max=li[i]
print('maximum number:',max)
