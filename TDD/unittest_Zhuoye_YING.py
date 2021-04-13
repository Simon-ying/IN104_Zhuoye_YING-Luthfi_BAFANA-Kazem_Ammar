import unittest
import subshape

class TestInput(unittest.TestCase):
    ''' the input for circle are x, y, rayon, r, g, b
        rayon>0 and 0<=r,g,b<256'''
    rayon1 = 0
    rayon2 = -1
    rgb1 = -1
    rgb2 = 256
    circle = subshape.Circle()
    def test_circleinput(self):
        self.assertRaises(subshape.RangeError, self.circle.create, 0,0,0,0,0,self.rayon1,)
        self.assertRaises(subshape.RangeError, self.circle.create, 0,0,0,0,0,self.rayon2,)
        self.assertRaises(subshape.RangeError, self.circle.create, 0,0,self.rgb1,0,0,1)
        self.assertRaises(subshape.RangeError, self.circle.create, 0,0,self.rgb2,0,0,1)
        self.assertRaises(subshape.RangeError, self.circle.create, 0,0,0,0,self.rgb2,1)
        
    ''' the input for rectangle are x, y, h, w, r, g, b
        h>0 and w>0 and 0<=r,g,b<256'''
    v = -1
    rgb1 = -1
    rgb2 = 256
    rect = subshape.Rect()
    def test_rectinput(self):
        self.assertRaises(subshape.RangeError, self.rect.create, 0,0,0,0,0,self.v,1)
        self.assertRaises(subshape.RangeError, self.rect.create, 0,0,0,0,0,1,self.v)
        self.assertRaises(subshape.RangeError, self.rect.create, 0,0,self.rgb1,0,0,1,1)
        self.assertRaises(subshape.RangeError, self.rect.create, 0,0,self.rgb2,0,0,1,1)
        self.assertRaises(subshape.RangeError, self.rect.create, 0,0,0,0,self.rgb2,1,1)
        
        
    ''' the input for triangle are x, y, q, w, e, g, b
        q,w,e>0 and 0<=r,g,b<256'''
    v = -1
    rgb1 = -1
    rgb2 = 256
    tri = subshape.Tri()
    def test_triinput(self):
        self.assertRaises(subshape.RangeError, self.tri.create, 0,0,0,0,0,self.v,1,1)
        self.assertRaises(subshape.RangeError, self.tri.create, 0,0,0,0,0,1,self.v,1)
        self.assertRaises(subshape.RangeError, self.tri.create, 0,0,0,0,0,1,1,self.v)
        self.assertRaises(subshape.RangeError, self.tri.create, 0,0,self.rgb1,0,0,1,1,1)
        self.assertRaises(subshape.RangeError, self.tri.create, 0,0,self.rgb2,0,0,1,1,1)
        self.assertRaises(subshape.RangeError, self.tri.create, 0,0,0,0,self.rgb2,1,1,1)
        
        
        
        
        
if __name__=='__main__':
    unittest.main()
    
    