# class point
class Point:
    # default_color = "red"
    # __(magic methods in python)

    def __init__(self, x, y):  # constructor
        self.x = x  # instance
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    # @classmethod
    # def zero(cls):
    #     return cls(0, 0)

    def draw(self):
        print(f"Point({self.x},{self.y})")


# Point.default_color = "yellow"
# point = Point(1, 2)  # point is object of class
# # print(point.x)
# # print(type(point))
# # print(isinstance(point, Point))
# print(point.default_color)
# point.draw()

# # another = Point(3, 4)
# another.draw()

# point = Point.zero()
# point.draw()

point = Point(1, 2)
print(str(point))
