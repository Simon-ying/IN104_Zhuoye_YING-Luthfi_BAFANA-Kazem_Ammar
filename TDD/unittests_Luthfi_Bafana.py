import unittest
import shape
import subshape

class TestCircle(unittest.TestCase):

    def test_get_area_circle(self):
        c = subshape.Circle()
        area = c.get_area()
        self.assertEqual(area, 3.14)
    

    def test_get_perimeter_circle(self):
        c = subshape.Circle()
        perimeter = c.get_perimeter()
        self.assertEqual(perimeter, -6.28)

class TestRect(unittest.TestCase):

    def test_get_area_rect(self):
        r = subshape.Rect()
        area = r.get_area()
        self.assertEqual(area, 0)

    def test_get_perimeter_rect(self):
        r = subshape.Rect()
        perimeter = r.get_perimeter()
        self.assertEqual(perimeter, 0)

if __name__ == '__main__':
    unittest.main()
