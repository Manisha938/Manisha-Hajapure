#Sum of all prime numbers between 1 to n
def prime_num(n):
    for num in range(2,n+1):
        c=0
        for i in range(1,num+1):
            if num %i==0:
                c=c+1
        if c==2:
           print(num)

n=int(input('enter the number:'))

prime_num(n)