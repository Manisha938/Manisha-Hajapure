def Armstrong(num,temp ):
    if temp == 0:
        return 0
    d = temp % 10
    return d*d*d + Armstrong(num,temp // 10)
    
num=int(input('enter number:'))
if Armstrong(num,num) == num :
   print(True)
else:
   print(False)


    