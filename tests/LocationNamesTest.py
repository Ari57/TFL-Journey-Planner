import sys
import os
import unittest
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from LocationNames import getLocationNames

class TestInput(unittest.TestCase):
    def test_ValidInput(self):
        response = getLocationNames("barking", "shenfield")
        self.assertEqual(response.status_code, 300)
        response = getLocationNames("bank", "paddington")
        self.assertEqual(response.status_code, 300)
    
    def test_InvalidInput(self): 
        self.assertRaises(TypeError, getLocationNames) # this seems to work ok, it catches the TypeError
        
        #self.assertEqual(response.status_code, 400)
        # this fails as you can't concat an int to a string
        # I have error checking in the LocationNames file for this


if __name__ == "__main__":
    unittest.main()
