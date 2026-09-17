"""The Adapter Pattern is a structural design pattern that allows two incompatible classes(two classes cannot 
work together directly because their interfaces (methods) are different.) to work together by converting one 
interface into another interface that the client expects."""

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


# Null Object Pattern
class clsDepartmentDB:
    departments = [
        clsDepartment(1, "CSE"),
        clsDepartment(2, "EEE")
    ]

    def get_department(self, department_id):
        for dept in self.departments:
            if dept.department_id == department_id:
                return dept

        return clsDepartment(0, "Department Name Not Found")


# Abstract Class
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
        return clsDepartmentDB().get_department(self.department_id)

    def write_info(self):
        University().get_university_info()
        print(f"Dr. {self.name}")
        print(f"Department: {self.department.department_name}")


class clsTeacherNonPhD(clsEmployee):
    def __init__(self):
        super().__init__()
        self.department_id = 0
        self.papers = 0

    @property
    def department(self):
        return clsDepartmentDB().get_department(self.department_id)

    def write_info(self):
        University().get_university_info()
        print(f"Mr. {self.name}")
        print(f"Department: {self.department.department_name}")


class clsOfficer(clsEmployee):
    def __init__(self):
        super().__init__()
        self.office = ""
        self.association_member = False

    def write_info(self):
        University().get_university_info()
        print(f"Officer: {self.name}")
        print(f"Office: {self.office}")


# Factory Pattern
class clsFacultyFactory:
    def get_teacher(
        self,
        qualification,
        name,
        dob,
        address,
        designation,
        department
    ):

        if qualification == "PhD":
            teacher = clsTeacherPhD()
        else:
            teacher = clsTeacherNonPhD()

        teacher.name = name
        teacher.date_of_birth = datetime.strptime(dob, "%d/%m/%Y")
        teacher.permanent_address = address
        teacher.designation = designation

        if department == "CSE":
            teacher.department_id = 1
        elif department == "EEE":
            teacher.department_id = 2

        return teacher


# Adapter Interface
class IEmployeeAdapter(ABC):

    @abstractmethod
    def get_employees(self):
        pass


# Legacy System 1
class clsLegacyTeachingHRSystem:

    def get_teachers(self):
        return [
            ["PhD", "Arif", "01/01/1979",
             "Jashore", "Assistant Professor", "CSE"],

            ["MSc", "Rakib", "01/01/1982",
             "Khulna", "Lecturer", "EEE"]
        ]


# Legacy System 2
class clsLegacyOfficialHRSystem:

    def get_officers(self):
        return [
            ["Reza", "01/01/1979",
             "Jashore", "Clark (Grade-2)", "HR"],

            ["Hakim", "01/01/1982",
             "Khulna", "Clark (Grade-3)", "ACC"]
        ]


# Teacher Adapter
class clsTeacherAdapter(IEmployeeAdapter):

    def get_employees(self):

        employees = []

        legacy = clsLegacyTeachingHRSystem()

        for emp in legacy.get_teachers():

            factory = clsFacultyFactory()

            employees.append(
                factory.get_teacher(
                    emp[0],
                    emp[1],
                    emp[2],
                    emp[3],
                    emp[4],
                    emp[5]
                )
            )

        return employees


# Officer Adapter
class clsOfficerAdapter(IEmployeeAdapter):

    def get_employees(self):

        employees = []

        legacy = clsLegacyOfficialHRSystem()

        for emp in legacy.get_officers():

            officer = clsOfficer()

            officer.name = emp[0]
            officer.date_of_birth = datetime.strptime(emp[1],"%d/%m/%Y")
            officer.permanent_address = emp[2]
            officer.designation = emp[3]
            officer.office = emp[4]

            employees.append(officer)

        return employees


def main():

    adapter = clsTeacherAdapter()

    print("######### Teacher List from Legacy System ##########")

    for employee in adapter.get_employees():
        employee.write_info()

    adapter = clsOfficerAdapter()

    print("######### Officer List from Legacy System ##########")

    for employee in adapter.get_employees():
        employee.write_info()


if __name__ == "__main__":
    main()


"""
Teaching HR System
        |
        v
 Teacher Adapter
        |
        v
 Teacher Objects
        |
        v
 employee.write_info()

------------------------------------------------

Official HR System
        |
        v
 Officer Adapter
        |
        v
 Officer Objects
        |
        v
 employee.write_info()
 """    