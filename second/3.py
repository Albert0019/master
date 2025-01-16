from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def compare_area(self, other):
        if self.area() > other.area():
            return f"Area of {self.__class__.__name__} is greater"
        elif self.area() < other.area():
            return f"Area of {self.__class__.__name__} is smaller"
        else:
            return "Areas are equal"

    def compare_perimeter(self, other):
        if self.perimeter() > other.perimeter():
            return f"Perimeter of {self.__class__.__name__} is greater"
        elif self.perimeter() < other.perimeter():
            return f"Perimeter of {self.__class__.__name__} is smaller"
        else:
            return "Perimeters are equal"


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return 4 * self.side


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self) -> float:
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


# Test
square = Square(4)
rectangle = Rectangle(4, 5)
print(square.compare_area(rectangle))  # Area of Square is smaller
print(square.compare_perimeter(rectangle))  # Perimeter of Square is smaller