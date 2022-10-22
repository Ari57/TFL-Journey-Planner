import sys
import os
import unittest
import requests
import random
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from LocationNames import getLocationNames, FromArray, ToArray
from JourneySteps import receiveResults
from secret.keys import pk, sk

class TestInput(unittest.TestCase):
    def test_ValidInput(self):
        getLocationNames("goodmayes", "canary wharf")
        for x in range(0,2):
            i = random.randint(0,len(FromArray)) - 1
            j = random.randint(0,len(ToArray)) - 1
            FromInput = FromArray[i]
            ToInput = ToArray[j]
            url = "https://api.tfl.gov.uk/journey/journeyresults/"+FromInput+"/to/"+ToInput+"?app_id="+pk+"&app_key="+sk
            response = requests.get(url)
            receiveResults(response)
            print("------------------------------------------")
        

# by this point in the code, all error checking will have been completed
# however in this particular test, some tests fail
# this is because some locations aren't exact enough, and the api brings up multiple locations with similar names
# the function will look for a key with the json, and won't find it, causing an error

if __name__ == "__main__":
    unittest.main()
