import math

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Example usage
shape_type = input("Enter shape type (circle, rectangle, square, triangle): ")

if shape_type == "circle":
    radius = float(input("Enter radius: "))
    shape = Circle(radius)
elif shape_type == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    shape = Rectangle(length, width)
elif shape_type == "square":
    side = float(input("Enter side length: "))
    shape = Square(side)
elif shape_type == "triangle":
    base = float(input("Enter base length: "))
    height = float(input("Enter height: "))
    side1 = float(input("Enter side 1 length: "))
    side2 = float(input("Enter side 2 length: "))
    side3 = float(input("Enter side 3 length: "))
    shape = Triangle(base, height, side1, side2, side3)
else:
    print("Invalid shape type.")
    exit()

print(f"{shape_type.capitalize()} area: {shape.area()}")
print(f"{shape_type.capitalize()} perimeter: {shape.perimeter()}")

