# """
# Get people details from file, show their name, age, finance
# we want to have Person with a defined str method
#
# For the runner we will want Employees, Students and Working Students, implement these classes
# """
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.__class__}: Name:{self.name}, {self.age} years old"
#
#
# class Employee(Person):
#     def __init__(self, name, age, rate, working_hours):
#         Person.__init__(self, name, age)
#         self.rate = rate
#         self.working_hours = working_hours
#
#     def show_finance(self):
#         return self.rate * self.working_hours
#
#
# class Student(Person):
#     def __init__(self, name, age, scholarship):
#         Person.__init__(self, name, age)
#         self.scholarship = scholarship
#
#     def show_finance(self):
#         return self.scholarship
#
#
# class WorkingStudent(Employee, Student):
#     def __init__(self, name, age, rate, working_hours, scholarship):
#         super().__init__(name, age, rate, working_hours)
#         super().__init__(name, age, scholarship)
#
#     def show_finance(self):
#         return self.rate * self.working_hours + self.scholarship
#
#
# ws = WorkingStudent('asd', 20, 5, 10, 100)
# print(ws)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"Class: {self.__class__}, name: {self.name}, age: {self.age}"
#
#
# class Employee(Person):
#     def __init__(self, name, age, rate, hours):
#         super().__init__(self, name, age)
#         self.rate = rate
#         self.hours = hours
#
#     def finance(self):
#         return self.rate * self.hours
#
#
# class Student(Person):
#     def __init__(self, name, age, scholarship):
#         super().__init__(name, age)
#         self.scholarship = scholarship
#
#     def finance(self):
#         return self.scholarship
#
#
# class WorkingStudent(Employee, Student):
#     def __init__(self, name, age, rate, hours, scholarship):
#         Employee.__init__(self, name, age, rate, hours)
#         Student.__init__(self, name, age, scholarship)
#
#     def finance(self):
#         return self.rate * self.hours + self.scholarship
#
#
# if __name__ == '__main__':
#     viorel = WorkingStudent("Viorel", 22, 10, 80, 200)
#     print(viorel)
#     print(viorel.finance())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Class: {self.__class__}, name:{self.name}, age:{self.age}"


class Employee(Person):
    def __init__(self, name, age, rate, hours):
        super().__init__( name, age)
        self.rate = rate
        self.hours = hours

    def finance(self):
        return self.rate * self.hours


class Student(Person):
    def __int__(self, name, age, scholarship):
        super().__init__( self, name, age)
        self.scholarship = scholarship

    def finance(self):
        return self.scholarship


class WorkingStudent(Employee, Student):
    def __int__(self, name, age, rate, hours, scholarship):
        Employee.__init__(self, name, age, rate, hours)
        Student.__init__(self,name,age,scholarship)

    def finance(self):
        return self.rate * self.hours + self.scholarship

if __name__ == '__main__':
    viorel = WorkingStudent("viorel",22,10, 80,200)
    print(viorel)
    print(viorel.finance())
    people_types = {}
    attr_person = lines[0].split(',')
    name, age, rate, hours = attr_person
    viorel = people_types[len(attr_person)](name, age, rate, hours)
