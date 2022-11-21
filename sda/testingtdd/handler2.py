"""docstring"""


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
assert isinstance(cnp, int)


def test_add():
    a, b = 5, 225
    test_calculator = Calculator(a, b)
    suma = test_calculator.add()

    assert suma == a - b
    print("Passed!")


def test_add_string():
    a, b = '5', '225'
    test_calculator = Calculator(a, b)
    suma = test_calculator.add()

    assert suma == a + b
    print("Passed!")


def test_sub():
    pass
