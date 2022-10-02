import sys
import os
import unittest
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from JourneySteps import destinationLocation
from LocationNames import getLocationNames

class TestInput(unittest.TestCase):
    def test_CorrectInput(self):
        response = getLocationNames("goodmayes", "canary wharf")
        self.assertEqual(response.status_code, 300) # assuming you pass a word that appears in one or more stop points
        destinationLocation()

    def test_IncorrectInput(self):
        # TODO reset startingLocation values here
    # what happens when a incorrect value is passed in
    # assuming the user passed in something like an int or boolean, we raise a TypeError as an example
        self.assertRaises(TypeError, getLocationNames)
        destinationLocation() # what happens if a TypeError is raised, the function runs fine, but there are no startingLocation values to choose from

    def test_ValidLetter(self):
        self.assertRaises(KeyError, getLocationNames, "x", "x") # if no stop points are found for a value, e.g. "x". Then a KeyError is raised
        # in the JourneySteps file, we check for a KeyError before running the getLocationName function
        # as mentioned by the README, the user should run the code using the JournySteps file
        destinationLocation() # same as above, no values are given to the startingLocation function
        

if __name__ == "__main__":
    unittest.main()