"""combines multiple teacher data sources into a single interface."""

from abc import ABC, abstractmethod
from datetime import datetime


# =========================
# Singleton Pattern
# =========================

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


# =========================
# Department
# =========================

class clsDepartment:
    def __init__(self, department_id=0, department_name=""):
        self.department_id = department_id
        self.department_name = department_name


class clsDepartmentDB:
    departments = [
        clsDepartment(1, "CSE"),
        clsDepartment(2, "EEE")
    ]

    def get_department(self, department_id):
        for department in self.departments:
            if department.department_id == department_id:
                return department

        return clsDepartment(
            0,"Department Name Not Found"
        )


# =========================
# Abstract Employee
# =========================

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


# =========================
# Teacher PhD
# =========================

class clsTeacherPhD(clsEmployee):

    def __init__(self):
        super().__init__()
        self.department_id = 0
        self.papers = 0

    @property
    def department(self):
        return clsDepartmentDB().get_department(
            self.department_id
        )

    def write_info(self):
        University().get_university_info()

        print("Teacher Info")
        print(f"Name: Dr. {self.name}")
        print(f"Department: {self.department.department_name}")
        print(f"Papers: {self.papers}")


# =========================
# Teacher Non PhD
# =========================

class clsTeacherNonPhD(clsEmployee):

    def __init__(self):
        super().__init__()
        self.department_id = 0
        self.papers = 0

    @property
    def department(self):
        return clsDepartmentDB().get_department(
            self.department_id
        )

    def write_info(self):
        University().get_university_info()

        print("Teacher Info")
        print(f"Name: Mr. {self.name}")
        print(f"Department: {self.department.department_name}")
        print(f"Papers: {self.papers}")


# =========================
# Officer
# =========================

class clsOfficer(clsEmployee):

    def __init__(self):
        super().__init__()
        self.office = ""
        self.association_member = False

    def write_info(self):
        University().get_university_info()

        print("Officer Info")
        print(f"Name: {self.name}")
        print(f"Office: {self.office}")


# =========================
# Staff
# =========================

class clsStaff(clsEmployee):

    def __init__(self):
        super().__init__()
        self.overtime = 0

    def write_info(self):
        University().get_university_info()

        print("Staff Info")
        print(f"Name: {self.name}")
        print(f"Overtime: {self.overtime}")


# =========================
# Factory Pattern
# =========================

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
        teacher.date_of_birth = datetime.strptime(dob,"%d/%m/%Y")

        teacher.permanent_address = address
        teacher.designation = designation

        if department == "CSE":
            teacher.department_id = 1
        elif department == "EEE":
            teacher.department_id = 2

        return teacher


# =========================
# Adapter Interface
# =========================

class IEmployeeAdapter(ABC):

    @abstractmethod
    def get_employees(self):
        pass


# =========================
# Legacy Systems
# =========================

class clsCollegeTeacherHRSystem:

    def fetch_college_teachers(self):
        return [
            ["BL College",
             "Afroza Sultana XYZ",
             "01/01/1979",
             "Jashore",
             "Assistant Professor",
             "CSE"],

            ["MM College",
             "Moni Khan",
             "01/01/1982",
             "Khulna",
             "Lecturer",
             "EEE"]
        ]


class clsLegacyTeachingHRSystem:

    def fetch_teachers(self):
        return [
            ["PhD",
             "Arif",
             "01/01/1979",
             "Jashore",
             "Assistant Professor",
             "CSE"],

            ["MSc",
             "Rakib",
             "01/01/1982",
             "Khulna",
             "Lecturer",
             "EEE"]
        ]


class clsLegacyOfficialHRSystem:

    def fetch_officers(self):
        return [
            ["Reza 1234",
             "01/01/1979",
             "Jashore",
             "Clark (Grade-2)",
             "HR"],

            ["Hakim",
             "01/01/1982",
             "Khulna",
             "Clark (Grade-3)",
             "ACC"]
        ]


"""
    CollegeTeacherHRSystem
          ↓
          ├── TeacherAdapter ──► Employee Objects
          ▲
          │
    LegacyTeachingHRSystem
"""    

# =========================
# Teacher Adapter
# =========================

class clsTeacherAdapter(IEmployeeAdapter):

    def __init__(self, college_hr_system):
        self.college_hr_system = college_hr_system

    def get_employees(self):

        employees = []

        factory = clsFacultyFactory()

        for emp in self.college_hr_system.fetch_college_teachers():

            employees.append(
                factory.get_teacher(
                    "MSc",
                    emp[1],
                    emp[2],
                    emp[3],
                    emp[4],
                    emp[5]
                )
            )

        legacy = clsLegacyTeachingHRSystem()

        for emp in legacy.fetch_teachers():

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


# =========================
# Officer Adapter
# =========================

class clsOfficerAdapter(IEmployeeAdapter):

    def get_employees(self):

        employees = []

        legacy = clsLegacyOfficialHRSystem()

        for emp in legacy.fetch_officers():

            officer = clsOfficer()

            officer.name = emp[0]
            officer.office = emp[4]
            officer.designation = emp[3]

            employees.append(officer)

        return employees


# =========================
# Main
# =========================

def main():

    adapters = [
        clsTeacherAdapter(
            clsCollegeTeacherHRSystem()
        ),
        clsOfficerAdapter()
    ]

    print(
        "######### List of Employees ##########"
    )

    for adapter in adapters:
        for employee in adapter.get_employees():
            employee.write_info()
            print()


if __name__ == "__main__":
    main()