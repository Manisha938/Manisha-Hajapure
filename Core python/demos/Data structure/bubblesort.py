def bubbleSort(li):
    size = len(li)
    for i in range(1,size):
        for j in range(0, size - 1):
            if(li [j] > li [j + 1]):
                li[j], li[j +1]= li[j + 1],li[j]
                #print(li)


li=[90,95,80,70,40,30,60]
print("befor sorting:",li)
bubbleSort(li)
print('after sorting:', li)                

