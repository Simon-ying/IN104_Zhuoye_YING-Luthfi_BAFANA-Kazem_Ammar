# -*- coding: utf-8 -*-

class Shape:
    center_x = 0
    center_y = 0
    color = (0, 0, 0)
    def __init__(self, x, y, r, g, b):
        self.center_x = x
        self.center_y = y
        self.color = (r, g, b)
    
    def get_center(self):
        return self.center_point
    def get_area():
        return
    def get_perimeter():
        return
    
class Circle(Shape):
    rayon=0
    def __init__(self, x, y, r, g, b, rayon):
        super(Circle,self).__init__(x, y, r, g, b)
        self.rayon = rayon
    def get_area(self):
        return 3.14*self.r*self.r
    def get_perimeter(self):
        return 2*3.14*self.r


class Rect(Shape):
    height = 0
    width = 0
    def __init__(self, x, y, r, g, b, h, w):
        super(Rect,self).__init__(x, y, r, g, b)
        self.height = h
        self.width = w
    def get_area(self):
        return self.height * self.width
    def get_perimeter(self):
        return 2*(self.height + self.width)