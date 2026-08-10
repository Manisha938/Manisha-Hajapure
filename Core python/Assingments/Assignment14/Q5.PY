#5. Write a Python program to find the longest common prefix of all
#strings. Use the Python set.
frist=["flower","flow","fight"]
prefix=frist[0]

for word in frist[1:]:
    while word[:len(prefix)]!=prefix:
        prefix=prefix[:-1]
        if prefix == "":
            break
    print("longest common prefix:",prefix)
    


