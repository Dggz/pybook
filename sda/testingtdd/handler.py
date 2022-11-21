"""
docstring
"""

"""
Exercise 1
Create a Calculator class in which you will implement the following 
operations: addition, subtraction, multiplication, division. Write tests that will test the previously mentioned methods.

The class might look like this:
"""


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self, reverse=False):
        if reverse:
            return self.b - self.a
        else:
            return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def div(self, reverse=False):
        if reverse:
            return self.b / self.a
        else:
            return self.a / self.b


lenovo = Calculator(12, 43)
print(f"Adunare: {lenovo.add()}")
print(f"Div: {lenovo.div()}")
print(f"Div reverse: {lenovo.div(False)}")

nume, cnp = '', 0
# input(nume)
# input(cnp)

assert type(nume) == str

import ipdb; ipdb.set_trace()
# comentariu
assert isinstance(cnp, int)

var = 'variabila'

def test_add():
    a, b = 5, 225
    test_calculator = Calculator(a, b)
    suma = test_calculator.add()

    assert suma == a + b
    print("Passed!")


def test_add_string():
    a, b = '5', '225'
    test_calculator = Calculator(a, b)
    suma = test_calculator.add()

    assert suma == a + b
    print("Passed!")


test_add()
test_add_string()
