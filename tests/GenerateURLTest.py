import sys
import os
import random
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from LocationNames import getLocationNames, FromArray, ToArray
from JourneySteps import generateURL

# sometimes I get 200 or 300 as a response code, would be good to test for both 

class TestInput(unittest.TestCase):
    def test_response_200(self):
        getLocationNames("barking", "shenfield")
            
        i = random.randint(0,len(FromArray)) - 1
        j = random.randint(0,len(ToArray)) - 1
        
        FromInput = FromArray[i]
        ToInput = ToArray[j]
        response = generateURL(FromInput, ToInput)

        self.assertEqual(response.status_code, 200, "Response code was " + str(response.status_code))

    def test_response_300(self):
        getLocationNames("barking", "shenfield")
    
        i = random.randint(0,len(FromArray)) - 1
        j = random.randint(0,len(ToArray)) - 1
        
        FromInput = FromArray[i]
        ToInput = ToArray[j]
        response = generateURL(FromInput, ToInput)

        self.assertEqual(response.status_code, 300, "Response code was " + str(response.status_code))

    def test_incorrectResponse(self):
        getLocationNames("barking", "shenfield")
        # pass an incorrect value to see if the try/except statement gets triggered
        i = random.randint(0,len(FromArray)) - 1
        j = random.randint(0,len(ToArray)) - 1
        FromInput = FromArray[i] + "fefe"
        ToInput = ToArray[j] + "gegw"
        generateURL(FromInput, ToInput)



if __name__ == "__main__":
    unittest.main()
