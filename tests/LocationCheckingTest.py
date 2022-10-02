import sys
import os
import unittest
import random

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from JourneySteps import LocationChecking, generateURL
from LocationNames import getLocationNames, FromArray, ToArray

class TestInput(unittest.TestCase):
    def test_CorrectInput(self):
        getLocationNames("goodmayes", "romford")
        # test to see if we get a 200/300 (multiple choices) response when entering correct input values
        FromInput = "Goodmayes, Goodmayes Station"
        ToInput = "Romford (London), Romford Station"
        response = LocationChecking(generateURL(FromInput, ToInput))
        self.assertEqual(response.status_code, 300) # assuming you pass a word that appears in one or more stop points
        
# def multipleLocations():
#     # what happens when we pass in a value that has multiple locations
#     getLocationNames("goodmayes", "romford")
#     # Romford (London), Romford Station is one of these locations
#     # I don't know of any others to test with, but they probably exist
#     LocationChecking(generateURL(startingLocation(), destinationLocation()))

# def oneLocation():
#     # what happens when we pass in a value that has no extra locations
#     getLocationNames("goodmayes", "canary wharf")
#     LocationChecking(generateURL(startingLocation(), destinationLocation()))

    # the function has nothing to do, so it would just pass on to the receiveResults function, if we called it here

if __name__ == "__main__":
    unittest.main(exit=False)