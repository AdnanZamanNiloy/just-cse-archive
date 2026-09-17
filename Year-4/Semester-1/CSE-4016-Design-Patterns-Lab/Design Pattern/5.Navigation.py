"""Navigation means accessing one object's data through another object reference.
Here:

1. teacher is a clsTeacher object.
2. teacher.department returns a clsDepartment object.
3. .name accesses the name attribute of that department object.

So you are navigating from Teacher → Department."""

from abc import ABC, abstractmethod
from datetime import datetime


class clsDepartment:
    def __init__(self):
        self.department_id = 0
        self.name = ""


class clsEmployee(ABC):
    def __init__(self):
        self.name = ""
        self.date_of_birth = datetime.today()
        self.sex = "M"
        self.permanent_address = ""
        self.current_address = ""
        self.phone = ""
        self.designation = ""

    @abstractmethod
    def write_info(self):
        pass


class clsTeacher(clsEmployee):
    def __init__(self):
        super().__init__()
        self.department_id = 0
        self.papers = 0

    @property
    def department(self):
        dept = clsDepartment()

        if self.department_id == 1:
            dept.department_id = 1
            dept.name = "CSE"
        elif self.department_id == 2:
            dept.department_id = 2
            dept.name = "EEE"

        return dept

    def write_info(self):
        print("Teacher Info:")
        print("-------------------")
        print(f"Name: {self.name}")
        print(f"Department: {self.department.name}") # Navigation
        print(f"Papers: {self.papers}")


class clsOfficer(clsEmployee):
    def __init__(self):
        super().__init__()
        self.office = ""
        self.association_member = False

    def write_info(self):
        print("Officer Info:")
        print("-------------------")
        print(f"Name: {self.name}")
        print(f"Office: {self.office}")
        print(f"Association: {self.association_member}")


class clsStaff(clsEmployee):
    def __init__(self):
        super().__init__()
        self.overtime = 0.0

    def write_info(self):
        print("Staff Info:")
        print("-------------------")
        print(f"Name: {self.name}")
        print(f"Overtime: {self.overtime}")


def main():
    employees = []

    teacher1 = clsTeacher()
    teacher1.name = "Nasim"
    teacher1.department_id = 1
    teacher1.papers = 2
    employees.append(teacher1)

    teacher2 = clsTeacher()
    teacher2.name = "Nasim"
    teacher2.department_id = 2
    teacher2.papers = 2
    employees.append(teacher2)

    officer = clsOfficer()
    officer.name = "Ahdab"
    officer.office = "HR"
    officer.association_member = True
    employees.append(officer)

    staff = clsStaff()
    staff.name = "Kuddus"
    staff.overtime = 10.75
    employees.append(staff)

    for emp in employees:
        emp.write_info()
        print()


if __name__ == "__main__":
    main()