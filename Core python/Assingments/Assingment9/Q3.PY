#Reverse number using recrusive
def reverse(num,rev):
    if num == 0:
        return rev
        d= num % 10
        return reverse (num // 10,rev *10 +d)

num=int(input('enter a number:'))
print(reverse (num, 0))