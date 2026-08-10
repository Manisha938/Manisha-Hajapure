def gen(n):
    for i in range(1,n+1):
        yield(i)
g=gen(5)
print(next(g))
print("ruk jara")
print(next(g))
print("next no ko ane de")
print(next(g))
print("mera no ko aa gaya")
print(next(g))
print("sadi karni hei ruk ja")
print(next(g))