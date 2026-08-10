from EmpManage import EmpManage
def logIn():
    em=EmpManage()
    uId = input("Enter the user id: ")
    password = input("Enter the password: ")

    if uId == "admin" and password == "1234":

        while True:
            print("\nPlease select one option below")
            print("1. Add Employee")
            print("2. Display All Employee")
            print("3. Search Employee")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                em.AddEmp()
            elif choice == 2:
                em.DisplayEmp()
            elif choice ==3:
                em.SearchEmp()   
            elif choice == 4:
                em.UpdateEmp()
            elif choice == 5:
                em.DeleteEmp()
            elif choice == 6:
                print("Exit...")
                break
            else:
                print("Invalid Choice")

    else:
        print("Invalid User ID or Password")
logIn()
