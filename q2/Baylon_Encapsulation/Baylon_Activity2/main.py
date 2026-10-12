class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
        else:
            print("Width must be greater than 0.")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value > 0:
            self.__height = value
        else:
            print("Height must be greater than 0.")

    def area(self):
        return self.__width * self.__height


rectangle = Rectangle(10, 5)

print("Width:", rectangle.width)
print("Height:", rectangle.height)
print("Area:", rectangle.area())

rectangle.width = 8
rectangle.height = 4

print("Updated width:", rectangle.width)
print("Updated height:", rectangle.height)
print("Updated area:", rectangle.area())