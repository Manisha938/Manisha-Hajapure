#project
class Employee:
    def __init__(self, eid, name, department, salary):
        self.eid = eid
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print("-----------------------------------")
        print("Employee ID :", self.eid)
        print("Name        :", self.name)
        print("Department  :", self.department)
        print("Salary      :", self.salary)
        print("-----------------------------------")


emp_list = []


def add_employee():
    eid = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    emp = Employee(eid, name, department, salary)
    emp_list.append(emp)
    print("Employee Added Successfully.")


def display_employee():
    if len(emp_list) == 0:
        print("No Employee Found.")
    else:
        for emp in emp_list:
            emp.display()


def search_employee():
    eid = int(input("Enter Employee ID to Search: "))

    for emp in emp_list:
        if emp.eid == eid:
            print("Employee Found")
            emp.display()
            return

    print("Employee Not Found.")


def update_employee():
    eid = int(input("Enter Employee ID to Update: "))

    for emp in emp_list:
        if emp.eid == eid:
            emp.name = input("Enter New Name: ")
            emp.department = input("Enter New Department: ")
            emp.salary = float(input("Enter New Salary: "))
            print("Employee Updated Successfully.")
            return

    print("Employee Not Found.")


def delete_employee():
    eid = int(input("Enter Employee ID to Delete: "))

    for emp in emp_list:
        if emp.eid == eid:
            emp_list.remove(emp)
            print("Employee Deleted Successfully.")
            return

    print("Employee Not Found.")


while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        display_employee()

    elif choice == 3:
        search_employee()

    elif choice == 4:
        update_employee()

    elif choice == 5:
        delete_employee()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")