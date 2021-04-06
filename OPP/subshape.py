# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:33:54 2021

@author: Simon
"""


class Circle(Shape):
    rayon=0
    def __init__(self, x, y, r, g, b, rayon):
        super(Circle,self).__init__(x, y, r, g, b)
        self.rayon = rayon
    def get_area(self):
        return 3.14*self.rayon*self.rayon
    def get_perimeter(self):
        return 2*3.14*self.rayon


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
    
    
if __name__ == '__main__':
    circle1 = Circle(1, 5, 0, 255, 255, 6)
    rect1 = Rect(5, 3, 255, 0, 255, 3, 4)
    print("The area of circle1 is :" + str(circle1.get_area()))
    print("The area of rect1 is :" + str(rect1.get_area()))
    print("The perimeter of circle1 is :" + str(circle1.get_perimeter()))
    print("The perimeter of rect1 is :" + str(rect1.get_perimeter()))