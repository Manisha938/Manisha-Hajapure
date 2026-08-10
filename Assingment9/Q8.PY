#WAP calculate the m to n power
def power(m,n):
    if n == 0:
        return 1
    return m * power (m,n-1)

m=int(input('enter base(m):'))
n=int(input('enter base(n):'))
print("Answer=",power(m,n))