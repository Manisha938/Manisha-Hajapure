def selectionSort(li):
    size=len(li)
    for i in range (0,size - 1):
        min_ind = i
        for j in range (i + 1 , size ):
            if (li[min_ind]> li[j]):
                min_ind = j 


        li[i],li[min_ind]=li[min_ind],li[i]
        print(li)
li=[60,50,40,30,20,10]
selectionSort(li) 
print('after sorting:',li)    