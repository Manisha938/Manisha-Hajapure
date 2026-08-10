li=[12,30,40,56,68,89]

for i in range(len(li)):
    for j in range(len(li)-1):
        if li[j]> li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print("sorted list:",li)
print("second largest number:",li)

