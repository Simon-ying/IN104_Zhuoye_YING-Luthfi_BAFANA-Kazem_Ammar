import unittest

import subshape

class TestCircle(unittest.TestCase):

    def test_get_area_circle(self):
        c = Circle(1,1,r,g,b,1)
        area = c.get_area()
        self.assertEqual(area, 3.14)
    

    def test_get_perimeter_circle(self):
        c = Circle(1,1,r,g,b,1)
        perimeter = c.get_perimeter()
        self.assertEqual(perimeter, 6.28)

class TestRect(unittest.TestCase):

    def test_get_area_rect(self):
        r = Rect(1,1,r,g,b,1,2,5)
        area = r.get_area()
        self.assertEqual(area, 10)

    def test_get_perimeter_rect(self):
        r = Rect(1,1,r,g,b,1,2,5)
        perimeter = r.get_perimeter()
        self.assertEqual(perimeter, 14)

if __name__ == '__main__':
    unittest.main()
