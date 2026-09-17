"""The Builder Pattern is a creational design pattern used to construct complex objects step by step.
Instead of creating a large object with a huge constructor, you build it piece by piece.
"""
from abc import ABC, abstractmethod
from datetime import datetime


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
        for dept in self.departments:
            if dept.department_id == department_id:
                return dept

        return clsDepartment(0,"Department Name Not Found")


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


class clsTeacherPhD(clsEmployee):

    def __init__(
        self,
        name="",
        date_of_birth=None,
        sex="M",
        permanent_address="",
        current_address="",
        phone="",
        designation="",
        department_id=0,
        papers=0
    ):
        super().__init__()
        
        #These values replace the defaults from the parent class.
        self.name = name
        self.date_of_birth = date_of_birth or datetime.today()
        self.sex = sex
        self.permanent_address = permanent_address
        self.current_address = current_address
        self.phone = phone
        self.designation = designation

        self.department_id = department_id
        self.papers = papers

    @property
    def department(self):
        return clsDepartmentDB().get_department(
            self.department_id
        )

    def write_info(self):
        print(f"Dr. {self.name}")
        print(f"Department: {self.department.department_name}")


class clsTeacherNonPhD(clsEmployee):

    def __init__(
        self,
        name="",
        date_of_birth=None,
        sex="M",
        permanent_address="",
        current_address="",
        phone="",
        designation="",
        department_id=0,
        papers=0
    ):
        super().__init__()

        self.name = name
        self.date_of_birth = date_of_birth or datetime.today()
        self.sex = sex
        self.permanent_address = permanent_address
        self.current_address = current_address
        self.phone = phone
        self.designation = designation
        self.department_id = department_id
        self.papers = papers

    @property
    def department(self):
        return clsDepartmentDB().get_department(
            self.department_id
        )

    def write_info(self):
        print(f"Mr. {self.name}")
        print(f"Department: {self.department.department_name}")


# ==========================
# Builder Pattern
# ==========================

class clsTeacherBuilder:

    def __init__(self):
        self.name = ""
        self.date_of_birth = datetime.today()
        self.sex = "M"
        self.permanent_address = ""
        self.current_address = ""
        self.phone = ""
        self.designation = ""
        self.department_id = 0
        self.papers = 0

    def set_name(self, name):
        self.name = name
        return self

    def set_date_of_birth(self, dob):
        self.date_of_birth = dob
        return self

    def set_sex(self, sex):
        self.sex = sex
        return self

    def set_p_address(self, address):
        self.permanent_address = address
        return self

    def set_c_address(self, address):
        self.current_address = address
        return self

    def set_phone(self, phone):
        self.phone = phone
        return self

    def set_designation(self, designation):
        self.designation = designation
        return self

    def set_department_id(self, department_id):
        self.department_id = department_id
        return self

    def set_papers(self, papers):
        self.papers = papers
        return self

    def create_teacher_phd(self):
        return clsTeacherPhD(
            self.name,
            self.date_of_birth,
            self.sex,
            self.permanent_address,
            self.current_address,
            self.phone,
            self.designation,
            self.department_id,
            self.papers
        )

    def create_teacher_non_phd(self):
        return clsTeacherNonPhD(
            self.name,
            self.date_of_birth,
            self.sex,
            self.permanent_address,
            self.current_address,
            self.phone,
            self.designation,
            self.department_id,
            self.papers
        )


# Example Usage

teacher = (
    clsTeacherBuilder()
    .set_name("Arif")
    .set_date_of_birth(datetime.strptime("01/01/1979", "%d/%m/%Y"))
    .set_p_address("Jashore")
    .set_designation("Assistant Professor")
    .set_department_id(1)
    .create_teacher_phd()
)

teacher.write_info()

"""
Why Builder Pattern Here?

Because Teacher has many attributes:

name
date_of_birth
sex
permanent_address
current_address
phone
designation
department_id
papers

Instead of passing all of them in a huge constructor, the Builder Pattern lets you construct the object step by step.
"""