import math

class Shape:
    def __init__(self):
        self.area = 0
        self.radius = 0
        self.side = 0
        self.b = 0
        self.h = 0
        self.w = 0
        self.l = 0

    # circle
    def set_radius(self, radius):
        self.radius = radius

    def get_circle_area(self):
        self.area = math.pi * self.radius ** 2
        return self.area

    # square
    def set_side(self, side):
        self.side = side

    def get_square_area(self):
        self.area = self.side ** 2
        return self.area

    # rectangle
    def set_width_length(self, w, l):
        self.w = w
        self.l = l

    def get_rectangle_area(self):
        self.area = self.w * self.l
        return self.area

    # triangle
    def set_height_base(self,b,h):
       self.b = b
       self.h = h

    def get_triangle_area(self):
        self.area = 1 / 2 * self.b * self.h
        return self.area

