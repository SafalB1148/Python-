class Shape:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def get_area(self):
        return self.side1 * self.side2  # Default area calculation for a rectangle or square

    def __str__(self):
        return f'The area of this {self.__class__.__name__} is {self.get_area()}'


class Rectangle(Shape):
    def __init__(self, side1, side2):
        super().__init__(side1, side2)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # Square has equal sides


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(base, height)

    def get_area(self):
        return 0.5 * self.side1 * self.side2  # Formula for the area of a triangle


# Example Usage
rectangle = Rectangle(5, 10)
square = Square(4)
triangle = Triangle(3, 6)

print(rectangle)  # Output: The area of this Rectangle is 50
print(square)     # Output: The area of this Square is 16
print(triangle)   # Output: The area of this Triangle is 9
