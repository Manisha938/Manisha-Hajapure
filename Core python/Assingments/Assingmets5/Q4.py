#WAP to print Armstrong number within a given range
start=int(input('enter start:'))
end=int(input('enter end:'))
for num in range(start,end+1):
    temp=num
    total=0
    digits=len(str(num))

    while temp > 0:
        digit=temp%10
        total=total+(digit**digits)
        temp=temp//10

        if total== num:
            print(num)

