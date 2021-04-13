# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:33:54 2021

@author: Simon
"""
from shape import *
class RangeError(ValueError): pass

class Circle(Shape):
    rayon=0
    
    # init a circle
    def __init__(self):
        self.x = self.y = self.r = self.g = self.b = self.rayon = -1
        
    def isinit(self):
        return not(self.rayon==-1 and self.r==-1 and self.g==-1 and self.b==-1)
    
    def create(self, x, y, r, g, b, rayon):
        if rayon<=0:
            raise RangeError("rayon should be positif")
        if (r<0 or r>255):
            raise RangeError("r should in [0, 255]")
        if (b<0 or b>255):
            raise RangeError("g should in [0, 255]")
        if (g<0 or g>255):
            raise RangeError("b should in [0, 255]")
        
        
        
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        self.rayon = rayon
        return self.isinit()
    
    def get_area(self):
        return 3.14*self.rayon*self.rayon
    def get_perimeter(self):
        return 2*3.14*self.rayon


class Rect(Shape):
    height = 0
    width = 0
    def __init__(self):
        self.x = self.y = self.r = self.g = self.b = self.h = self.w = -1
        
    def isinit(self):
        return not(self.w==-1 and self.h==-1 and self.r==-1 and self.g==-1 and self.b==-1)
    
    def create(self, x, y, r, g, b, h, w):
        if h<0 or w<0:
            raise RangeError("h, w should be positif")
        if (r<0 or r>255):
            raise RangeError("r should in [0, 255]")
        if (b<0 or b>255):
            raise RangeError("g should in [0, 255]")
        if (g<0 or g>255):
            raise RangeError("b should in [0, 255]")
        
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        self.height = h
        self.width = w
        return self.isinit()
    def get_area(self):
        return self.height * self.width
    def get_perimeter(self):
        return 2*(self.height + self.width)

class Tri(Shape):
    q = w = e = -1
    def __init__(self):
        x = y = r = g = b = -1
        
    def isinit(self):
        return not(self.q==-1 and self.w==-1 and self.e==-1 and self.r==-1 and self.g==-1 and self.b==-1)
    
    def create(self, x, y, r, g, b, q, w, e):
        if q<0 or w<0 or e<0:
            raise RangeError("h, w,e should be positif")
        if (r<0 or r>255):
            raise RangeError("r should in [0, 255]")
        if (b<0 or b>255):
            raise RangeError("g should in [0, 255]")
        if (g<0 or g>255):
            raise RangeError("b should in [0, 255]")
        
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        self.q = q
        self.w = w
        self.e = e
        return self.isinit()
    def get_area(self):
        p = (q+w+e)/2
        return (p*(p-a)*(p-b)*(p-c))**(1/2)
    def get_perimeter(self):
        return self.q + self.w + self.e
    

    
    
if __name__ == '__main__':
    circle1 = Circle()
    circle1.create(1, 5, 0, 255, 255, 6)
    rect1 = Rect()
    rect1.create(5, 3, 255, 0, 255, 3, 4)
    print("The area of circle1 is :" + str(circle1.get_area()))
    print("The area of rect1 is :" + str(rect1.get_area()))
    print("The perimeter of circle1 is :" + str(circle1.get_perimeter()))
    print("The perimeter of rect1 is :" + str(rect1.get_perimeter()))
