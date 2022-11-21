from abc import ABC, abstractmethod
from copy import copy, deepcopy
from dataclasses import dataclass

# class Rectangle(Shape):
#     def __init__(self, a: int, b: int):
#         self.a = a
#         self.b = b
#
#     def __repr__(self) -> str:
#         return f"Rectangle(a={self.a}, b={self.b})"
#
#     def __eq__(self, other) -> bool:
#         return isinstance(other, Rectangle) and (self.a, self.b) == (other.a, other.b)
#
#     def circuit(self) -> float:
#         return 2 * (self.a + self.b)
#
#     def area(self) -> float:
#         return self.a * self.b


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


@dataclass
class Rectangle(Shape):
    a: int
    b: int

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


if __name__ == '__main__':
    # dr_str = Rectangle('3', '5')
    dr = Rectangle(3, 4)
    numbers = [1, 2, 3, [4, 5]]
    just_numbers = numbers

    shallow = copy(numbers)
    shallow.append(87)
    shallow[3] = 5

    deep = deepcopy(numbers)

    print(help(dr))
    just_numbers = [i for i in numbers if isinstance(i, int)]
    for e in just_numbers:
        if not isinstance(e, int):
            just_numbers.remove(e)
