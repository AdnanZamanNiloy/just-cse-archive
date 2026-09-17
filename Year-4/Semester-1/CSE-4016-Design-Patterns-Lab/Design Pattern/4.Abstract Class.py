from abc import ABC, abstractmethod
from datetime import datetime


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
        self.department = ""
        self.papers = 0

    def write_info(self):
        print("Teacher Info:")
        print("-------------------")
        print(f"Name:              {self.name}")
        print(f"Date of Birth:     {self.date_of_birth.strftime('%d/%m/%Y')}")
        print(f"Sex:               {self.sex}")
        print(f"Permanent Address: {self.permanent_address}")
        print(f"Current Address:   {self.current_address}")
        print(f"Phone:             {self.phone}")
        print(f"Designation:       {self.designation}")
        print(f"Department:        {self.department}")
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
        print(f"Date of Birth:     {self.date_of_birth.strftime('%d/%m/%Y')}")
        print(f"Sex:               {self.sex}")
        print(f"Permanent Address: {self.permanent_address}")
        print(f"Current Address:   {self.current_address}")
        print(f"Phone:             {self.phone}")
        print(f"Designation:       {self.designation}")
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
        print(f"Date of Birth:     {self.date_of_birth.strftime('%d/%m/%Y')}")
        print(f"Sex:               {self.sex}")
        print(f"Permanent Address: {self.permanent_address}")
        print(f"Current Address:   {self.current_address}")
        print(f"Phone:             {self.phone}")
        print(f"Designation:       {self.designation}")
        print(f"Overtime:          {self.overtime}")


def main():
    employees = [None] * 3

    teacher = clsTeacher()
    teacher.name = "Nasim"
    teacher.date_of_birth = datetime.strptime("01/01/1979", "%d/%m/%Y")
    teacher.sex = "M"
    teacher.permanent_address = "Magura"
    teacher.current_address = "Mirpur"
    teacher.phone = "01730016854"
    teacher.designation = "Assistant Director"
    teacher.department = "ITOCD"
    teacher.papers = 2

    employees[0] = teacher

    officer = clsOfficer()
    officer.name = "Ahdab"
    officer.date_of_birth = datetime.strptime("01/01/1975", "%d/%m/%Y")
    officer.sex = "M"
    officer.permanent_address = "Dinajpur"
    officer.current_address = "Kalyanpur"
    officer.phone = "01712345678"
    officer.designation = "Clark (Grade-1)"
    officer.office = "HR"
    officer.association_member = True

    employees[1] = officer

    staff = clsStaff()
    staff.name = "Kuddus"
    staff.date_of_birth = datetime.strptime("01/01/1980", "%d/%m/%Y")
    staff.sex = "M"
    staff.permanent_address = "Dinajpur"
    staff.current_address = "Kalyanpur"
    staff.phone = "01712345678"
    staff.designation = "Sweeper"
    staff.overtime = 10.75

    employees[2] = staff

    for emp in employees:
        emp.write_info()
        print()


if __name__ == "__main__":
    main()