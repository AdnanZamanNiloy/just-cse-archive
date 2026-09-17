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


def main():
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

    teacher2 = clsTeacher()

    teacher2.name = "Arman"
    teacher2.date_of_birth = datetime.strptime("01/01/1979", "%d/%m/%Y")
    teacher2.sex = "M"
    teacher2.permanent_address = "Magura"
    teacher2.current_address = "Mirpur"
    teacher2.phone = "01730016854"
    teacher2.designation = "Assistant Director"
    teacher2.department = "ITOCD"
    teacher2.papers = 2

    teacher1 = teacher2

    teacher2.name = "Shahin"

    teacher1.write_info()
    teacher2.write_info()


if __name__ == "__main__":
    main()