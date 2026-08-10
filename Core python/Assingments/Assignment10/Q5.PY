#Accept a number from user and check if this element is present in the list or
#not. Also tell how many times it is present in the list.
list=[10,20,30,40,40,50,50,70]

num=int(input('enter the number:'))

count=0
for i in list:
    if i == num:
        count = count +1

if count > 0:
    print('elements is present in list',count)
    #print('it is present',count,)
else:
    print('elements is not present in the list')