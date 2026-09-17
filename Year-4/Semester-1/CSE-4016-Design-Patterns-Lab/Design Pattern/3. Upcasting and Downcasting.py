from datetime import datetime


class clsEmployee:
    def __init__(self):
        self.name = ""
        self.date_of_birth = datetime.today()
        self.sex = "M"
        self.permanent_address = ""
        self.current_address = ""
        self.phone = ""
        self.designation = ""

    def write_info(self):
        print("Employee Info:")
        print("-------------------")
        print(f"Name:              {self.name}")
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
        print(f"Designation:       {self.designation}")
        print(f"Department:        {self.department}")
        print(f"Papers:            {self.papers}")


def main():
    employees = [None] * 2

    teacher1 = clsTeacher()
    teacher1.name = "Nasim"
    teacher1.designation = "Assistant Professor"
    teacher1.department = "CSE"
    teacher1.papers = 20

    employees[0] = teacher1

    teacher2 = clsTeacher()
    teacher2.name = "Abdullah"
    teacher2.department = "EEE"
    teacher2.papers = 5

    employees[1] = teacher2

    for i in range(2):

        # Downcasting (not needed in Python)
        teacher_dc = employees[i]

        teacher_dc.write_info()

        # Upcasting (automatic in Python)
        employee_uc = teacher_dc

        employee_uc.write_info()

        print()


if __name__ == "__main__":
    main()