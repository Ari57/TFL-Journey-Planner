import sys
import os
import random
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from JourneySteps import TrainStatus, generateURL, LocationChecking
from LocationNames import getLocationNames, FromArray, ToArray

class TestInput(unittest.TestCase):
    def test_SetValue(self):
        # seeing if the function actually works with valid values
        response = LocationChecking(generateURL("Goodmayes, Goodmayes Station", 
        "Canary Wharf, Canary Wharf Rail Station"))

        TrainStatus(response)

    def test_AnyValue(self):
        FromValues = ["goodmayes", "canary wharf", "romford", "barking", "greenwich"]
        ToValues = ["acton", "ealing", "west", "north", "south"]
        
        for x in range(0,len(FromValues)):
            getLocationNames(FromValues[x], ToValues[x])
            for o in range(0,2):
                i = random.randint(0,len(FromArray)) - 1
                j = random.randint(0,len(ToArray)) - 1
                FromInput = FromArray[i]
                ToInput = ToArray[j]

                response = LocationChecking(generateURL(FromInput, ToInput))
                TrainStatus(response)

                # the error that LocationChecking deals with, will occur here

if __name__ == "__main__":
    unittest.main()