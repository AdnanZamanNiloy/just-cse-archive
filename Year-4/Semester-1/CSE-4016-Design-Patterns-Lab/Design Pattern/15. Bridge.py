"""The Bridge Pattern is a structural design pattern that separates an
 abstraction from its implementation so that both can vary independently.
 Instead of creating many subclasses for every possible combination, Bridge
  uses composition to connect two independent hierarchies.
 Without Bridge Pattern, you would need classes for every combination:

TeacherForeignTour
TeacherNationalTour
TeacherLocalTour

OfficerForeignTour
OfficerNationalTour
OfficerLocalTour

StaffForeignTour
StaffNationalTour
StaffLocalTour"""

from abc import ABC, abstractmethod
from datetime import datetime


# ==========================
# Department
# ==========================

class clsDepartment:
    def __init__(self):
        self.department_id = 0
        self.department_name = ""


# ==========================
# Tour Type Hierarchy
# Strategy Pattern
# ==========================

class clsTourType(ABC):

    def __init__(self, basic_salary):
        self._name = ""
        self._basic_salary = basic_salary

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_tada(self):
        pass


class clsForeignTour(clsTourType):

    def __init__(self, basic_salary):
        super().__init__(basic_salary)
        self._name = "Foreign Tour"

    def get_tada(self):
        return self._basic_salary * 0.5


class clsNationalTour(clsTourType):

    def __init__(self, basic_salary):
        super().__init__(basic_salary)
        self._name = "National Tour"

    def get_tada(self):
        return self._basic_salary * 0.3


class clsLocalTour(clsTourType):

    def __init__(self, basic_salary):
        super().__init__(basic_salary)
        self._name = "Local Tour"

    def get_tada(self):
        return self._basic_salary * 0.1


# ==========================
# Employee Base Class
# ==========================

class clsEmployee(ABC):

    def __init__(self):
        self.name = ""
        self.date_of_birth = datetime.today()
        self.sex = "M"
        self.permanent_address = ""
        self.current_address = ""
        self.phone = ""
        self.designation = ""
        self.basic_salary = 0.0

        self._tour_type = None

    @property
    def tour_type(self):
        return self._tour_type

    @tour_type.setter
    def tour_type(self, value):
        self._tour_type = value

    @abstractmethod
    def get_tada(self):
        pass

    @abstractmethod
    def write_info(self):
        pass


# ==========================
# Teacher
# ==========================

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
            dept.department_name = "CSE"

        elif self.department_id == 2:
            dept.department_id = 2
            dept.department_name = "EEE"

        return dept

    def get_tada(self):
        print(f"Tour Type:         {self._tour_type.name}")
        print(f"Amount:            {self._tour_type.get_tada()}")

    def write_info(self):

        print("Teacher Info:")
        print("-------------------")
        print(f"Name:              {self.name}")
        print(f"Date of Birth:     {self.date_of_birth}")
        print(f"Sex:               {self.sex}")
        print(f"Permanent Address: {self.permanent_address}")
        print(f"Current Address:   {self.current_address}")
        print(f"Phone:             {self.phone}")
        print(f"Designation:       {self.designation}")
        print(f"Department:        {self.department.department_name}")
        print(f"Papers:            {self.papers}")
        print(f"Basic Salary:      {self.basic_salary}")


# ==========================
# Officer
# ==========================

class clsOfficer(clsEmployee):

    def __init__(self):
        super().__init__()

        self.office = ""
        self.association_member = False

    def get_tada(self):
        print(f"Tour Type:         {self._tour_type.name}")
        print(f"Amount:            {self._tour_type.get_tada()}")

    def write_info(self):

        print("Officer Info:")
        print("-------------------")
        print(f"Name:              {self.name}")
        print(f"Date of Birth:     {self.date_of_birth}")
        print(f"Sex:               {self.sex}")
        print(f"Permanent Address: {self.permanent_address}")
        print(f"Current Address:   {self.current_address}")
        print(f"Phone:             {self.phone}")
        print(f"Designation:       {self.designation}")
        print(f"Office:            {self.office}")
        print(f"Association:       {self.association_member}")
        print(f"Basic Salary:      {self.basic_salary}")


# ==========================
# Staff
# ==========================

class clsStaff(clsEmployee):

    def __init__(self):
        super().__init__()

        self.overtime = 0.0

    def get_tada(self):
        print(f"Tour Type:         {self._tour_type.name}")
        print(f"Amount:            {self._tour_type.get_tada()}")

    def write_info(self):

        print("Staff Info:")
        print("-------------------")
        print(f"Name:              {self.name}")
        print(f"Date of Birth:     {self.date_of_birth}")
        print(f"Sex:               {self.sex}")
        print(f"Permanent Address: {self.permanent_address}")
        print(f"Current Address:   {self.current_address}")
        print(f"Phone:             {self.phone}")
        print(f"Designation:       {self.designation}")
        print(f"Overtime:          {self.overtime}")
        print(f"Basic Salary:      {self.basic_salary}")


# ==========================
# Main
# ==========================

def main():

    teacher1 = clsTeacher()

    teacher1.name = "Nasim"
    teacher1.date_of_birth = datetime.strptime(
        "01/01/1979",
        "%d/%m/%Y"
    )
    teacher1.sex = "M"
    teacher1.permanent_address = "Magura"
    teacher1.current_address = "Mirpur"
    teacher1.phone = "01730016854"
    teacher1.designation = "Assistant Director"
    teacher1.basic_salary = 100000
    teacher1.department_id = 1
    teacher1.papers = 50

    # Foreign Tour
    teacher1.tour_type = clsForeignTour(teacher1.basic_salary)

    teacher1.write_info()
    teacher1.get_tada()

    print()

    # National Tour
    teacher1.tour_type = clsNationalTour(teacher1.basic_salary)

    teacher1.write_info()
    teacher1.get_tada()

    print()

    # Local Tour
    teacher1.tour_type = clsLocalTour(
        teacher1.basic_salary
    )

    teacher1.write_info()
    teacher1.get_tada()


if __name__ == "__main__":
    main()