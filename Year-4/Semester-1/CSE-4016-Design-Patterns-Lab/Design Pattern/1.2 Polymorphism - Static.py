from datetime import datetime


class clsEmployee:
    employee_counter = 0  # static/class variable

    def __init__(self):
        self.name = ""
        self.date_of_birth = datetime.today()
        self.sex = "M"
        self.permanent_address = ""
        self.current_address = ""
        self.phone = ""
        self.designation = ""

        clsEmployee.employee_counter += 1

    @property
    def number_of_employees(self):
        return clsEmployee.employee_counter

    def write_info(self):
        print("Employee Info:")
        print("-------------------")
        print(f"Name:              {self.name}")
        print(f"Date of Birth:     {self.date_of_birth.strftime('%d/%m/%Y')}")
        print(f"Sex:               {self.sex}")
        print(f"Permanent Address: {self.permanent_address}")
        print(f"Current Address:   {self.current_address}")
        print(f"Phone:             {self.phone}")
        print(f"Designation:       {self.designation}")


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


def main():
    employees = [None] * 3

    teacher1 = clsTeacher()
    teacher1.name = "Nasim"
    teacher1.date_of_birth = datetime.strptime("01/01/1979", "%d/%m/%Y")
    teacher1.sex = "M"
    teacher1.permanent_address = "Magura"
    teacher1.current_address = "Mirpur"
    teacher1.phone = "01730016854"
    teacher1.designation = "Assistant Director"
    teacher1.department = "ITOCD"
    teacher1.papers = 2

    employees[0] = teacher1

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

    teacher2 = clsTeacher()
    teacher2.name = "Abdullah"
    teacher2.date_of_birth = datetime.strptime("01/01/1980", "%d/%m/%Y")
    teacher2.sex = "M"
    teacher2.permanent_address = "Dinajpur"
    teacher2.current_address = "Kalyanpur"
    teacher2.phone = "01712345678"
    teacher2.designation = "Clark (Grade-3)"
    teacher2.department = "ITOCD"
    teacher2.papers = 2

    employees[2] = teacher2

    for emp in employees:
        emp.write_info()
        print("\n")

    print("Total Number of Employees:", teacher1.number_of_employees)


if __name__ == "__main__":
    main()