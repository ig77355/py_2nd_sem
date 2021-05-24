import math

# code taken from the Shapes.py until 27th line
class Shape:
    def __init__(self, a, b):
        self.set_params(a, b)

    def set_params(self, a, b):
        self._a = a
        self.b = b

    def get_a(self):
        return self._a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


class Rectangle(Shape):
    def calc_surface(self):
        return self._a * self.b

    def swap_sides(self):
        a = self._a
        b = self.b
        self._a = b
        self.b = a


# Isosceles triangle
class IsoscelesTriangle(Shape):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.a = None

    # Surface
    def calc_surface(self):
        # triangle has sides: a, b, b
        if self._a / 2 < self.b:
            return 1 / 2 * self._a * math.sqrt(pow(self.b, 2) - (pow(self._a, 2) / 4))
        # triangle has sides: a, a, b
        if self.b / 2 < self._a:
            return 1 / 2 * self.b * math.sqrt(pow(self._a, 2) - (pow(self.b, 2) / 4))

    # Perimeter
    def calc_perimeter(self):
        # triangle with sides: a, b, b
        if self._a / 2 < self.b:
            return 2 * self.b + self._a
        # triangle with sides: a, a, b
        if self.b / 2 < self._a:
            return 2 * self._a + self.b


t = IsoscelesTriangle(10, 5)
print('Surface of the isosceles triangle: ' + str(t.calc_surface()))
print('Perimeter of the isosceles triangle: ' + str(t.calc_perimeter()))


# Equilateral triangle
class EquilateralTriangle:
    def __init__(self, a):
        self._a = a
        self.set_params(a)

    def set_params(self, a):
        pass

    # Surface
    def calc_surface(self):
        return (math.sqrt(3) / 4) * self._a ** 2

    # Perimeter
    def calc_perimeter(self):
        return 3 * self._a


t1 = EquilateralTriangle(7)
print('Surface of the equilateral triangle: ' + str(t1.calc_surface()))
print('Perimeter of the equilateral triangle: ' + str(t1.calc_perimeter()))


# Square
class Square(Rectangle):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, a)

    # Surface
    def calc_surface(self):
        return super().calc_surface()

    # Perimeter
    def calc_perimeter(self):
        return 4 * self._a


s = Square(13)
print('Surface of the square: ' + str(s.calc_surface()))
print('Perimeter of the square: ' + str(s.calc_perimeter()))
