#WAP  dum of series of n numbers
def SumOfSeries(n):
    if n == 0:
        return 0
    else:
        return n+ SumOfSeries (n-1)

n=int(input('enter a number:'))
res=(SumOfSeries(n))
print(res)

