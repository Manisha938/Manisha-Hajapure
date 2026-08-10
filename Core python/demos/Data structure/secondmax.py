li=[34,57,680 ,42,23,650]

max1=li[0]
max2=li[0]

for i in range(1 ,len(li)):
    if li[i]> max1:
        max2 = max1
        max1 = li[i]
    elif li[i] > max2:
        max2 = li[i]


print("second maximum numner:",max2)