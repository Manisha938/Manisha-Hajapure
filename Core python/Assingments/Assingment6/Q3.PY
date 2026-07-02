#Q3
for i in range(1,5):
    for j in range(1,5-i):
        print(' ', end=' ')

    num=1 

    for j in range(1,i+1):
       print(num,end='  ')
       num = num * (i-j)//j
    print()