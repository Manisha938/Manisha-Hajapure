#q7
for i in range(1,6):
    for j in range(1 ,6-i):
        print("  ", end =" ")

    for i in range(1, 2 * i):
        print( chr(64+i) , end="  ")
    print()
