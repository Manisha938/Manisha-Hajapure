#3. Python Program to Check if a Given Key Exists in a Dictionary or Not
#creating
student={
    "name":"manisha",
    "age":21,
    "grede":'A'
}

#accept key from user
key=input("enter the key to search:")

#check if key exist
if key in student:
    print("key is exist in the dict")
else:
    print("key does not exit in the dict")
