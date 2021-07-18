import math

class Shape:
    def __init__(self, shape):
        self.area = 0
        self.radius = 0
        self.side = 0
        self.b = 0
        self.h = 0
        self.w = 0
        self.l = 0
        self.shape = shape

    # circle
    def set_radius(self, radius):
        self.radius = radius

    # square
    def set_side(self, side):
        self.side = side

    # rectangle
    def set_width_length(self, w, l):
        self.w = w
        self.l = l

    # triangle
    def set_height_base(self,b,h):
       self.b = b
       self.h = h

    def get_area(self):
        if self.shape == 'c': # circle
            self.area = math.pi * self.radius ** 2

        elif self.shape == 's': # square
            self.area = self.side ** 2

        elif self.shape == 'r': # rectangle
            self.area = self.w * self.l

        elif self.shape == 't': # triangle
            self.area = 1 / 2 * self.b * self.h

        else:
            self.area = 0 # no shape

        return self.area

