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
        return (
            self._basic_salary
            + self.get_house_rent()
            + self.get_conveyance()
        )

    def get_house_rent_conveyance_test(self):
        return (
            self._basic_salary
            + self.get_house_rent()
            + self.get_conveyance()
        )


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
# Appointment Types
# ==========================

class clsAppointmentType(ABC):

    def __init__(self):
        self._bonus_percent = 0.0

    @abstractmethod
    def get_bonus_percent(self):
        pass


class clsPermanent(clsAppointmentType):

    def __init__(self):
        super().__init__()
        self._bonus_percent = 1.0

    def get_bonus_percent(self):
        return self._bonus_percent


class clsTemporary(clsAppointmentType):

    def __init__(self):
        super().__init__()
        self._bonus_percent = 0.5

    def get_bonus_percent(self):
        return self._bonus_percent


class clsCasual(clsAppointmentType):

    def __init__(self):
        super().__init__()
        self._bonus_percent = 0.1

    def get_bonus_percent(self):
        return self._bonus_percent


# ==========================
# Salary Calculator
# ==========================

class clsSalaryCalculator:

    def __init__(self, basic_salary, appointment_type):
        self.basic_salary = basic_salary
        self.appointment_type = appointment_type

    def get_bonus(self):
        return (
            self.basic_salary
            * self.appointment_type.get_bonus_percent()
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

        self.grade = None

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

        # Composite Pattern
        self.employee_list = []

    def add(self, employee):
        self.employee_list.append(employee)

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

    def get_total_subordinate_salaries(self):

        total_salary = 0

        for employee in self.employee_list:
            total_salary += (
                employee.grade
                .get_house_rent_conveyance()
            )

        print(
            f"Sub Sal WO Bonus:  "
            f"{total_salary}"
        )

    def write_info(self):

        print("Teacher Info:")
        print("-------------------")
        print(f"Name:              {self.name}")
        print(f"Date of Birth:     {self.date_of_birth}")
        print(f"Sex:               {self.sex}")
        print(
            f"Permanent Address: "
            f"{self.permanent_address}"
        )
        print(
            f"Current Address:   "
            f"{self.current_address}"
        )
        print(f"Phone:             {self.phone}")
        print(
            f"Designation:       "
            f"{self.designation}"
        )
        print(
            f"Department:        "
            f"{self.department.department_name}"
        )
        print(f"Papers:            {self.papers}")
        print(f"Grade:             {self.grade.name}")

        self.get_total_subordinate_salaries()

        print(
            f"Basic Salary:      "
            f"{self.basic_salary}"
        )

        print(
            f"House Rent + Conv: "
            f"{self.grade.get_house_rent_conveyance()}"
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
        print(
            f"Association:       "
            f"{self.association_member}"
        )
        print(f"Grade:             {self.grade.name}")
        print(
            f"Basic Salary:      "
            f"{self.basic_salary}"
        )
        print(
            f"House Rent + Conv: "
            f"{self.grade.get_house_rent_conveyance()}"
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
        print(
            f"Basic Salary:      "
            f"{self.basic_salary}"
        )
        print(
            f"House Rent + Conv: "
            f"{self.grade.get_house_rent_conveyance()}"
        )


# ==========================
# Main
# ==========================

def main():

    employees = [None] * 4
    salary_calculators = [None] * 4

    teacher1 = clsTeacher()
    teacher1.name = "Nasim"
    teacher1.basic_salary = 100000
    teacher1.department_id = 1
    teacher1.papers = 2
    teacher1.grade = clsGradeA(
        teacher1.basic_salary
    )

    salary_calculators[0] = clsSalaryCalculator(
        teacher1.basic_salary,
        clsPermanent()
    )

    teacher2 = clsTeacher()
    teacher2.name = "Rahman"
    teacher2.basic_salary = 100000
    teacher2.department_id = 2
    teacher2.papers = 2
    teacher2.grade = clsGradeB(
        teacher2.basic_salary
    )

    salary_calculators[1] = clsSalaryCalculator(
        teacher2.basic_salary,
        clsTemporary()
    )

    officer = clsOfficer()
    officer.name = "Ahdab"
    officer.basic_salary = 100000
    officer.office = "HR"
    officer.association_member = True
    officer.grade = clsGradeA(
        officer.basic_salary
    )

    salary_calculators[2] = clsSalaryCalculator(
        officer.basic_salary,
        clsCasual()
    )

    teacher1.add(officer)

    staff = clsStaff()
    staff.name = "Kuddus"
    staff.basic_salary = 50000
    staff.overtime = 10.75

    # matches the C# code exactly
    staff.grade = clsGradeC(
        officer.basic_salary
    )

    salary_calculators[3] = clsSalaryCalculator(
        staff.basic_salary,
        clsPermanent()
    )

    teacher1.add(staff)

    employees[0] = teacher1
    employees[1] = teacher2
    employees[2] = officer
    employees[3] = staff

    for i in range(4):

        employees[i].write_info()

        print(
            f"Bonus Salary:      "
            f"{salary_calculators[i].get_bonus()}"
        )

        total_salary = (
            employees[i].basic_salary
            + employees[i].grade.get_house_rent_conveyance()
            + salary_calculators[i].get_bonus()
        )

        print(
            f"Total Salary:      "
            f"{total_salary}"
        )

        print()


if __name__ == "__main__":
    main()