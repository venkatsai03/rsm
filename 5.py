from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


# Creating instances of the shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Calculating the areas of the shapes
circle_area = circle.calculate_area()
rectangle_area = rectangle.calculate_area()
triangle_area = triangle.calculate_area()

# Displaying the areas of the shapes
print(f"Circle area: {circle_area}")
print(f"Rectangle area: {rectangle_area}")
print(f"Triangle area: {triangle_area}")
