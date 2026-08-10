from Hr import Hr
from Dev import Dev

class EmpManage:
    empDat = {}

    def AddEmp(self):
        print("......add Emp........")

        EmpId = int(input("enter the EmpId="))

        if EmpId in self.empDat:
            print("employee already exists...")
            return

        name = input("enter the name of EMP=")
        sal = float(input("enter the sal="))

        print("1. Hr")
        print("2. Developer")

        ch = int(input("enter the choice="))

        if ch == 1:
            com = float(input("enter the commission="))
            emp = Hr(EmpId, name, sal, com)

        elif ch == 2:
            bonus = float(input("enter the bonus="))
            emp = Dev(EmpId, name, sal, bonus)

        else:
            print("Invalid choice")
            return

        self.empDat[EmpId] = emp
        print("Employee added successfully")
