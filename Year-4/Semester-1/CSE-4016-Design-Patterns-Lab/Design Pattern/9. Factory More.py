"""Singleton + Factory + Null Object Pattern (NEW) + Abstract Class + Runtime Polymorphism"""

from abc import ABC, abstractmethod
from datetime import datetime


# Singleton Pattern
class University:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = "Jashore University of Science and Technology"
            cls._instance.address = "Ambottola, Jashore"
        return cls._instance

    def get_university_info(self):
        print("-------------------")
        print(f"{self.name}, {self.address}")
        print("-------------------")


class clsDepartment:
    def __init__(self, department_id=0, department_name=""):
        self.department_id = department_id
        self.department_name = department_name


# Department Database (Static Repository)
class DepartmentDB:
    departments = [
        clsDepartment(1, "CSE"),
        clsDepartment(2, "EEE")
    ]

    @staticmethod
    def get_department(department_id):
        for department in DepartmentDB.departments:
            if department.department_id == department_id:
                return department

        # Null Object Pattern
        return clsDepartment(0, "Department Name Not Found")


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


class clsTeacherPhD(clsEmployee):
    def __init__(self):
        super().__init__()
        self.department_id = 0
        self.papers = 0

    @property
    def department(self):
        return DepartmentDB.get_department(self.department_id)

    def write_info(self):
        University().get_university_info()

        print("Teacher Info:")
        print("-------------------")
        print(f"Name:              Dr. {self.name}")
        print(f"Date of Birth:     {self.date_of_birth}")
        print(f"Sex:               {self.sex}")
        print(f"Permanent Address: {self.permanent_address}")
        print(f"Current Address:   {self.current_address}")
        print(f"Phone:             {self.phone}")
        print(f"Designation:       {self.designation}")
        print(f"Department:        {self.department.department_name}")
        print(f"Papers:            {self.papers}")


class clsTeacherNonPhD(clsEmployee):
    def __init__(self):
        super().__init__()
        self.department_id = 0
        self.papers = 0

    @property
    def department(self):
        return DepartmentDB.get_department(self.department_id)

    def write_info(self):
        University().get_university_info()

        print("Teacher Info:")
        print("-------------------")
        print(f"Name:              Mr. {self.name}")
        print(f"Date of Birth:     {self.date_of_birth}")
        print(f"Sex:               {self.sex}")
        print(f"Permanent Address: {self.permanent_address}")
        print(f"Current Address:   {self.current_address}")
        print(f"Phone:             {self.phone}")
        print(f"Designation:       {self.designation}")
        print(f"Department:        {self.department.department_name}")
        print(f"Papers:            {self.papers}")


class clsOfficer(clsEmployee):
    def __init__(self):
        super().__init__()
        self.office = ""
        self.association_member = False

    def write_info(self):
        University().get_university_info()

        print("Officer Info:")
        print("-------------------")
        print(f"Name:              {self.name}")
        print(f"Office:            {self.office}")
        print(f"Association:       {self.association_member}")


class clsStaff(clsEmployee):
    def __init__(self):
        super().__init__()
        self.overtime = 0.0

    def write_info(self):
        University().get_university_info()

        print("Staff Info:")
        print("-------------------")
        print(f"Name:              {self.name}")
        print(f"Overtime:          {self.overtime}")


# Factory Pattern
class clsFacultyFactory:
    def get_teacher(self, qualification):

        if qualification == "PhD":
            teacher = clsTeacherPhD()

            teacher.name = "Nasim"
            teacher.date_of_birth = datetime.strptime(
                "01/01/1979", "%d/%m/%Y"
            )
            teacher.sex = "M"
            teacher.permanent_address = "Jhenaidah"
            teacher.current_address = "Jashore"
            teacher.phone = "01708524079"
            teacher.designation = "Assistant Professor"
            teacher.department_id = 1
            teacher.papers = 20

            return teacher

        elif qualification == "MSc":
            teacher = clsTeacherNonPhD()

            teacher.name = "Imran"
            teacher.date_of_birth = datetime.strptime(
                "01/01/1979", "%d/%m/%Y"
            )
            teacher.sex = "M"
            teacher.permanent_address = "Khulna"
            teacher.current_address = "Jashore"
            teacher.phone = "01712345678"
            teacher.designation = "Lecturer"
            teacher.department_id = 2
            teacher.papers = 2

            return teacher

        return None


def main():
    employees = [None] * 4

    faculty_factory = clsFacultyFactory()

    employees[0] = faculty_factory.get_teacher("PhD")
    employees[1] = faculty_factory.get_teacher("MSc")

    officer = clsOfficer()
    officer.name = "Ahdab"
    officer.office = "HR"
    officer.association_member = True
    employees[2] = officer

    staff = clsStaff()
    staff.name = "Kuddus"
    staff.overtime = 10.75
    employees[3] = staff

    for employee in employees:
        employee.write_info()
        print("\n")


if __name__ == "__main__":
    main()