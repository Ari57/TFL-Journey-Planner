import sys
import os
import random
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from JourneySteps import TrainStatus, generateURL, LocationChecking
from LocationNames import getLocationNames, FromArray, ToArray

class TestStringMethods(unittest.TestCase):
    def test_correct_status(self):
        self.assertEqual('foo'.upper(), 'FOO')

FromValues = ["goodmayes", "canary wharf", "romford", "barking", "greenwich"]
ToValues = ["acton", "ealing", "west", "north", "south"]

def correctStatus():
    for x in range(0,len(FromValues)):
        getLocationNames(FromValues[x], ToValues[x])
        for t in range(0,6):
            i = random.randint(0,len(FromArray)) - 1
            j = random.randint(0,len(ToArray)) - 1
            FromInput = FromArray[i]
            ToInput = ToArray[j]
    # what happens when we pass in values
    #TODO as the LocationChecking function runs a lot, I might need to use ICS codes instead
            response = LocationChecking(generateURL(FromInput, ToInput))
            TrainStatus(response)
    

def incorrectStatus():
        getLocationNames(1,2)
        for t in range(0,6):
            i = random.randint(0,len(FromArray)) - 1
            j = random.randint(0,len(ToArray)) - 1
            FromInput = FromArray[i]
            ToInput = ToArray[j]
    # what happens when we pass in values
        response = LocationChecking(generateURL(FromInput, ToInput)) # somehow mentions a "reportUnboundVariable" error here
        TrainStatus(response)
    

if __name__ == "__main__":
    #unittest.main()
    correctStatus()
    #incorrectStatus() # raises a TypeError that is handled in the LocationNames file