# #
# # def divide(x, y):
# #     return x / y
# #
# #
# # a = 3
# # b = [1, 0 , 2]
# # for elem in b:
# #     try:
# #         result = divide(a, elem)
# #     except ZeroDivisionError:
# #         print("nope")
# #     finally:
# #         print('I got here again!')
# #     # print(f"Result is: {result}")
#

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ma {self.age} years old"

    def __repr__(self):
        return f"Person: {self.name}, {self.age}"


# class Employee(Person):
#     def __init__(self, name, age, rate, working_hours):
#         super().__init__(name, age)
#         self.rate = rate
#         self.working_hours = working_hours
#
#     def show_finance(self):
#         return self.rate * self.working_hours
#
#
# class Student(Person):
#     def __init__(self, name, age, scholarship):
#         super().__init__(name, age)
#         self.scholarship = scholarship
#
#     def show_finance(self):
#         return self.scholarship
#
#
os1 = Person("Henry", 54)
print(os1)
os2 = Employee("Jack", 36, 20, 160)
os3 = Student("Agatha", 22, 1000)
print(os1)
print(os2)
print(os3)
#
#
#
#
#
#

class Employee(Person):
    def __init__(self, name, age, rate, working_hours):
        Person.__init__(self, name, age)
        self.rate = rate
        self.working_hours = working_hours

    def show_finance(self):
        return (self.rate * self.working_hours) * .9


class Student(Person):
    def __init__(self, name, age, scholarship):
        Person.__init__(self, name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


class WorkingStudent(Employee, Student):
    def __init__(self, name, age, rate, working_hours, scholarship):
        Employee.__init__(self, name, age, rate, working_hours)
        super().__init__(self, name, age, scholarship)

    def show_finance(self):
        return Employee.show_finance(self) + Student.show_finance(self)
