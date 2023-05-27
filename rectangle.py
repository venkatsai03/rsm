class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# Taking input for small rectangle
smallLength = float(input("Enter the length of the small rectangle: "))
smallWidth = float(input("Enter the width of the small rectangle: "))

smallRectangle = Rectangle(smallLength, smallWidth)

# Taking input for large rectangle
largeLength = float(input("Enter the length of the large rectangle: "))
largeWidth = float(input("Enter the width of the large rectangle: "))

largeRectangle = Rectangle(largeLength, largeWidth)

# Calculating the area and perimeter
smallArea = smallRectangle.calculate_area()
smallPerimeter = smallRectangle.calculate_perimeter()

largeArea = largeRectangle.calculate_area()
largePerimeter = largeRectangle.calculate_perimeter()

# Printing the results
print("Small Rectangle:")
print("Area:", smallArea)
print("Perimeter:", smallPerimeter)

print("\nLarge Rectangle:")
print("Area:", largeArea)
print("Perimeter:", largePerimeter)
