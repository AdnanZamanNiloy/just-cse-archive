from abc import ABC, abstractmethod
from datetime import datetime


# ==========================
# Department
# ==========================

class clsDepartment:
    def __init__(self):
        self.department_id = 0
        self.name = ""


# ==========================
# Appointment Types
# ==========================

class clsAppointmentType:

    def __init__(self):
        self._bonus_percent = 0.0

    def get_bonus_percent(self):
        return self._bonus_percent


class clsPermanent(clsAppointmentType):

    def __init__(self):
        super().__init__()
        self._bonus_percent = 1.0


class clsTemporary(clsAppointmentType):

    def __init__(self):
        super().__init__()
        self._bonus_percent = 0.5


class clsCasual(clsAppointmentType):

    def __init__(self):
        super().__init__()
        self._bonus_percent = 0.1


# ==========================
# Salary Calculator
# ==========================

class clsSalaryCalculator:

    def __init__(self, basic_salary, appointment_type):
        self._basic_salary = basic_salary
        self._appointment_type = appointment_type

    def get_bonus(self):
        return (
            self._basic_salary *
            self._appointment_type.get_bonus_percent()
        )


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
            dept.name = "CSE"

        elif self.department_id == 2:
            dept.department_id = 2
            dept.name = "EEE"

        return dept

    def write_info(self):

        print("Teacher Info:")
        print("-------------------")
        print(f"Name:              {self.name}")
        print(f"Date of Birth:     {self.date_of_birth.date()}")
        print(f"Sex:               {self.sex}")
        print(f"Permanent Address: {self.permanent_address}")
        print(f"Current Address:   {self.current_address}")
        print(f"Phone:             {self.phone}")
        print(f"Designation:       {self.designation}")
        print(f"Department:        {self.department.name}")
        print(f"Papers:            {self.papers}")


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
        print(f"Date of Birth:     {self.date_of_birth.date()}")
        print(f"Sex:               {self.sex}")
        print(f"Permanent Address: {self.permanent_address}")
        print(f"Current Address:   {self.current_address}")
        print(f"Phone:             {self.phone}")
        print(f"Designation:       {self.designation}")
        print(f"Office:            {self.office}")
        print(f"Association:       {self.association_member}")


# ==========================
# Staff
# ==========================

class clsStaff(clsEmployee):

    def __init__(self):
        super().__init__()

        self.over_time = 0.0

    def write_info(self):

        print("Staff Info:")
        print("-------------------")
        print(f"Name:              {self.name}")
        print(f"Date of Birth:     {self.date_of_birth.date()}")
        print(f"Sex:               {self.sex}")
        print(f"Permanent Address: {self.permanent_address}")
        print(f"Current Address:   {self.current_address}")
        print(f"Phone:             {self.phone}")
        print(f"Designation:       {self.designation}")
        print(f"Overtime:          {self.over_time}")


# ==========================
# Main
# ==========================

def main():

    employees = []
    salary_calculators = []

    # Teacher 1
    teacher1 = clsTeacher()

    teacher1.name = "Nasim"
    teacher1.date_of_birth = datetime.strptime("01/01/1979","%d/%m/%Y")
    teacher1.sex = "M"
    teacher1.permanent_address = "Magura"
    teacher1.current_address = "Mirpur"
    teacher1.phone = "01730016854"
    teacher1.designation = "Assistant Professor"
    teacher1.basic_salary = 100000
    teacher1.department_id = 1
    teacher1.papers = 2

    employees.append(teacher1)

    salary_calculators.append(
        clsSalaryCalculator(
            teacher1.basic_salary,
            clsPermanent()
        )
    )

    # Teacher 2
    teacher2 = clsTeacher()

    teacher2.name = "Rahman"
    teacher2.date_of_birth = datetime.strptime("01/01/1979","%d/%m/%Y")
    teacher2.sex = "M"
    teacher2.permanent_address = "Magura"
    teacher2.current_address = "Mirpur"
    teacher2.phone = "01730016854"
    teacher2.designation = "Lecturer"
    teacher2.basic_salary = 100000
    teacher2.department_id = 2
    teacher2.papers = 2

    employees.append(teacher2)

    salary_calculators.append(
        clsSalaryCalculator(
            teacher2.basic_salary,
            clsTemporary()
        )
    )

    # Officer
    officer = clsOfficer()

    officer.name = "Ahdab"
    officer.date_of_birth = datetime.strptime("01/01/1975","%d/%m/%Y")
    officer.sex = "M"
    officer.permanent_address = "Dinajpur"
    officer.current_address = "Kalyanpur"
    officer.phone = "01712345678"
    officer.designation = "Clark (Grade-1)"
    officer.basic_salary = 100000
    officer.office = "HR"
    officer.association_member = True

    employees.append(officer)

    salary_calculators.append(
        clsSalaryCalculator(
            officer.basic_salary,
            clsCasual()
        )
    )

    # Staff
    staff = clsStaff()

    staff.name = "Kuddus"
    staff.date_of_birth = datetime.strptime("01/01/1980","%d/%m/%Y")
    staff.sex = "M"
    staff.permanent_address = "Dinajpur"
    staff.current_address = "Kalyanpur"
    staff.phone = "01712345678"
    staff.designation = "Sweeper"
    staff.basic_salary = 50000
    staff.over_time = 10.75

    employees.append(staff)

    salary_calculators.append(
        clsSalaryCalculator(
            staff.basic_salary,
            clsPermanent()
        )
    )

    # Polymorphism
    for employee, calc in zip( employees,salary_calculators):

        employee.write_info()

        bonus = calc.get_bonus()

        print("-------------------")
        print(f"Basic Salary:      {employee.basic_salary}")
        print(f"Bonus:             {bonus}")
        print(
            f"Total Salary:      "
            f"{employee.basic_salary + bonus}"
        )
        print()


if __name__ == "__main__":
    main()