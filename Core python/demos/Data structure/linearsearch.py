def LinearSearch(li,searchEle):
    for i in range(0,len(li)):
        if(li[i]==searchEle):
            return i
    else:
        return 1

ele=90
li=[80,67,98,65,34,90,97]
res=LinearSearch(li,ele)

if(res!= -1):
    print(f"{ele}is present at index {res}")
else:
    print(f"{ele} is not present")
