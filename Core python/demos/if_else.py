#take the input
user_name='admin'
password='1234'

user_id=input("enter USER ID:")
Passw=input("enter password:")
if(user_id==user_name and Passw==password):
    print("Login successful")
else:
    print("Invalid credentials")