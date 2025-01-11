import math

class Shape:
    """Base class for different shapes."""
    def area(self):
        """Method to calculate area, meant to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override the area method.")

class Rectangle(Shape):
    """Rectangle shape class inheriting from Shape."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Circle shape class inheriting from Shape."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

