"""
Subtypes must be substitutable for their base types.
"""
from abc import ABC, abstractmethod


# bad approach
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "height"):
            self.__dict__["width"] = value
            self.__dict__["height"] = value


# good approach
class AShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class ARectangle(AShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class ASquare(AShape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2
