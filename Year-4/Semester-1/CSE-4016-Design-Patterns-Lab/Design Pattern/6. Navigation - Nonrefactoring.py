from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum


class clsDepartment:
    def __init__(self):
        self.department_id = 0
        self.name = ""


class AppointmentType(Enum):
    PERMANENT = 1
    TEMPORARY = 2
    CASUAL = 3


class clsSalaryCalculator:
    def __init__(self, basic_salary, appointment_type):
        self.basic_salary = basic_salary
        self.appointment_type = appointment_type

    def get_bonus(self):
        if self.appointment_type == AppointmentType.PERMANENT:
            return self.basic_salary * 1.0

        elif self.appointment_type == AppointmentType.TEMPORARY:
            return self.basic_salary * 0.5

        elif self.appointment_type == AppointmentType.CASUAL:
            return self.basic_salary * 0.1

        raise Exception("No Salary is defined.")


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
        print(f"Name:              {self.name}")
        print(f"Department:        {self.department.name}")
        print(f"Papers:            {self.papers}")


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
        print(f"Association:       {self.association_member}")


class clsStaff(clsEmployee):
    def __init__(self):
        super().__init__()
        self.overtime = 0.0

    def write_info(self):
        print("Staff Info:")
        print("-------------------")
        print(f"Name:              {self.name}")
        print(f"Overtime:          {self.overtime}")


def main():
    employees = []
    salary_calculators = []

    teacher1 = clsTeacher()
    teacher1.name = "Nasim"
    teacher1.basic_salary = 100000
    teacher1.department_id = 1
    teacher1.papers = 2

    employees.append(teacher1)
    salary_calculators.append(
        clsSalaryCalculator(
            teacher1.basic_salary,
            AppointmentType.PERMANENT
        )
    )

    teacher2 = clsTeacher()
    teacher2.name = "Rahman"
    teacher2.basic_salary = 100000
    teacher2.department_id = 2
    teacher2.papers = 2

    employees.append(teacher2)
    salary_calculators.append(
        clsSalaryCalculator(
            teacher2.basic_salary,
            AppointmentType.TEMPORARY
        )
    )

    officer = clsOfficer()
    officer.name = "Ahdab"
    officer.basic_salary = 100000
    officer.office = "HR"

    employees.append(officer)
    salary_calculators.append(
        clsSalaryCalculator(
            officer.basic_salary,
            AppointmentType.CASUAL
        )
    )

    staff = clsStaff()
    staff.name = "Kuddus"
    staff.basic_salary = 50000
    staff.overtime = 10.75

    employees.append(staff)
    salary_calculators.append(
        clsSalaryCalculator(
            staff.basic_salary,
            AppointmentType.PERMANENT
        )
    )

    for i in range(4):
        employees[i].write_info()

        bonus = salary_calculators[i].get_bonus()

        print("-------------------")
        print(f"Basic Salary:      {employees[i].basic_salary}")
        print(f"Bonus:             {bonus}")
        print(f"Total Salary:      {employees[i].basic_salary + bonus}")
        print()


if __name__ == "__main__":
    main()