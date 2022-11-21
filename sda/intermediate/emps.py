from datetime import date as dt


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Class: {self.__class__}, name:{self.name}, age:{self.age}"


class Student(Person):
    def __init__(self, name, age, scholarship):
        if self.is_name_correct(name):
            super().__init__(name, age)
            self.scholarship = scholarship

    # @instancemethod
    def show_finance(self):
        return self.scholarship

    @classmethod
    def create_from_string(cls, input_string):
        name, age, scholarship = input_string.split()
        age, scholarship = int(age), float(scholarship)
        if cls.is_name_correct(name):
            return cls(name, age, scholarship)

    @staticmethod
    def is_name_correct(name):
        if name[0].isupper() and len(name) > 1:
            return True
        return False


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age, country):
        if age < 21 and country == 'USA':
            return False
        if age < 18:
            return False
        return True

    @classmethod
    def emp_from_year(emp_class, name, year):
        return emp_class(name, dt.today().year - year)

    def __str__(self):
        return 'Employee Name: {} and Age: {}'.format(self.name, self.age)


# e1 = Employee('Dhiman', 25)
# print(e1)
# e2 = Employee.emp_from_year('Subhas', 1987)
# print(e2)
# print(Employee.is_adult(25, "UK"))
# print(Employee.is_adult(20, "USA"))
# print(Employee.is_adult(16, "EU"))


if __name__ == '__main__':
    stud = Student.create_from_string("Viorel 22 100")
    print(stud.show_finance())
    # print(Student.show_finance(stud))
    print()
