"""
The Composite Pattern is a structural design pattern that allows you to treat a single object and a group of objects 
in the same way. It organizes objects into a tree-like structure where a parent object can contain child objects. 
This makes it easy to work with complex hierarchies such as company organizational charts, file systems, and menu 
structures without writing separate code for individual objects and groups.

Scenario

Imagine a university hierarchy:

Teacher (Head of Department)
│
├── Officer (HR Officer)
└── Staff (Office Assistant)

Here:

1. Teacher can have subordinates (Officer, Staff)
2. Officer and Staff are also employees
3. All of them inherit from clsEmployee
"""

from abc import ABC, abstractmethod
from datetime import datetime


class clsDepartment:
    def __init__(self):
        self.department_id = 0
        self.department_name = ""


# ==========================
# Grade Hierarchy
# ==========================

class clsGrade(ABC):

    def __init__(self, basic_salary):
        self._name = ""
        self._basic_salary = basic_salary

    @property 
    def name(self):
        return self._name

    @abstractmethod
    def get_house_rent(self):
        pass
   
    @abstractmethod
    def get_conveyance(self):
        pass

    def get_house_rent_conveyance(self):
        return self.get_house_rent() + self.get_conveyance()




class clsGradeA(clsGrade):

    def __init__(self, basic_salary):
        super().__init__(basic_salary)
        self._name = "Grade A"

    def get_house_rent(self):
        return self._basic_salary * 0.5

    def get_conveyance(self):
        return self._basic_salary * 0.5


class clsGradeB(clsGrade):

    def __init__(self, basic_salary):
        super().__init__(basic_salary)
        self._name = "Grade B"

    def get_house_rent(self):
        return self._basic_salary * 0.3

    def get_conveyance(self):
        return self._basic_salary * 0.3


class clsGradeC(clsGrade):

    def __init__(self, basic_salary):
        super().__init__(basic_salary)
        self._name = "Grade C"

    def get_house_rent(self):
        return self._basic_salary * 0.1

    def get_conveyance(self):
        return self._basic_salary * 0.1


# ==========================
# Appointment Type Hierarchy
# ==========================

class clsAppointmentType(ABC):

    def __init__(self, basic_salary):
        self._basic_salary = basic_salary
        self._bonus_percent = 0.0

    @abstractmethod
    def get_bonus_percent(self):
        pass

    def get_bonus(self):
        return self._basic_salary * self._bonus_percent


class clsPermanent(clsAppointmentType):

    def __init__(self, basic_salary):
        super().__init__(basic_salary)
        self._bonus_percent = 1.0

    def get_bonus_percent(self):
        return self._bonus_percent


class clsTemporary(clsAppointmentType):

    def __init__(self, basic_salary):
        super().__init__(basic_salary)
        self._bonus_percent = 0.5

    def get_bonus_percent(self):
        return self._bonus_percent


class clsCasual(clsAppointmentType):

    def __init__(self, basic_salary):
        super().__init__(basic_salary)
        self._bonus_percent = 0.1

    def get_bonus_percent(self):
        return self._bonus_percent

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

        self.grade = None
        self.appointment_type = None

        # Composite Pattern
        self.employee_list = []

    def add(self, employee):
        self.employee_list.append(employee)

    def get_total_subordinate_salaries(self):

        total_salary = 0.0

        for employee in self.employee_list:

            total_salary += (
                employee.basic_salary
                + employee.grade.get_house_rent_conveyance()
                + employee.appointment_type.get_bonus()
            )

        return total_salary

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

    def write_info(self):

        print("Teacher Info:")
        print("-------------------")
        print(f"Name:              {self.name}")
        print(f"Department:        {self.department.department_name}")
        print(f"Papers:            {self.papers}")
        print(f"Grade:             {self.grade.name}")
        print(f"Basic Salary:      {self.basic_salary}")
        print(
            f"House Rent + Conv: "
            f"{self.grade.get_house_rent_conveyance()}"
        )
        print(
            f"Bonus:             "
            f"{self.appointment_type.get_bonus()}"
        )


# ==========================
# Officer
# ==========================

class clsOfficer(clsEmployee):

    def __init__(self):
        super().__init__()

        self.office = ""
        self.association_member = False

    def write_info(self):

        print("Officer Info:")
        print("-------------------")
        print(f"Name:              {self.name}")
        print(f"Office:            {self.office}")
        print(f"Grade:             {self.grade.name}")
        print(f"Basic Salary:      {self.basic_salary}")
        print(
            f"House Rent + Conv: "
            f"{self.grade.get_house_rent_conveyance()}"
        )
        print(
            f"Bonus:             "
            f"{self.appointment_type.get_bonus()}"
        )


# ==========================
# Staff
# ==========================

class clsStaff(clsEmployee):

    def __init__(self):
        super().__init__()

        self.overtime = 0.0

    def write_info(self):

        print("Staff Info:")
        print("-------------------")
        print(f"Name:              {self.name}")
        print(f"Overtime:          {self.overtime}")
        print(f"Grade:             {self.grade.name}")
        print(f"Basic Salary:      {self.basic_salary}")
        print(
            f"House Rent + Conv: "
            f"{self.grade.get_house_rent_conveyance()}"
        )
        print(
            f"Bonus:             "
            f"{self.appointment_type.get_bonus()}"
        )


# ==========================
# Main
# ==========================

def main():

    employees = [None] * 4

    teacher1 = clsTeacher()
    teacher1.name = "Nasim"
    teacher1.basic_salary = 100000
    teacher1.department_id = 1
    teacher1.papers = 2
    teacher1.grade = clsGradeA(teacher1.basic_salary)
    teacher1.appointment_type = clsPermanent(teacher1.basic_salary)

    teacher1.add(teacher1)

    teacher2 = clsTeacher()
    teacher2.name = "Rahman"
    teacher2.basic_salary = 100000
    teacher2.department_id = 2
    teacher2.papers = 2
    teacher2.grade = clsGradeB(teacher2.basic_salary)
    teacher2.appointment_type = clsTemporary(teacher2.basic_salary)

    officer = clsOfficer()
    officer.name = "Ahdab Added"
    officer.basic_salary = 100000
    officer.office = "HR"
    officer.association_member = True
    officer.grade = clsGradeA(officer.basic_salary)
    officer.appointment_type = clsCasual(officer.basic_salary)

    staff = clsStaff()
    staff.name = "Kuddus Added"
    staff.basic_salary = 50000
    staff.overtime = 10.75
    staff.grade = clsGradeC(staff.basic_salary)
    staff.appointment_type = clsPermanent(staff.basic_salary)

    teacher1.add(officer)
    teacher1.add(staff)

    employees[0] = teacher1
    employees[1] = teacher2
    employees[2] = officer
    employees[3] = staff

    for emp in employees:

        emp.write_info()

        total_salary = (
            emp.basic_salary
            + emp.grade.get_house_rent_conveyance()
            + emp.appointment_type.get_bonus()
        )

        print(f"Total Salary:      {total_salary}")

        print(
            f"Total Sub Salary:  "
            f"{emp.get_total_subordinate_salaries()}"
        )

        print()


if __name__ == "__main__":
    main()