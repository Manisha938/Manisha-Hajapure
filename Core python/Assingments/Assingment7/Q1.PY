#Q1
for i in range(1,6):
    for j in range(1,6-i):
        print(" ", end="")

        for j in range(1, 2*i):
            if j==1 or j== 2*i-1:
                print("*", end="  ")
            else:
                print("  ", end="  ")
        print()

    #lower
    for i in range(4,0,-1):
        for j in range(1,6-i):
            print(" ", end=" ")
            
        for j in range(1, 2*i):
            if j==1 or j==2*i-1:
               print("*",end=" ")
            else:
               print("  ", end=" ")
        print()
