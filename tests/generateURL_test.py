import sys
import os
import random
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from LocationNames import FromArray, ToArray
from JourneySteps import generateURL

def correctResponse():
    print("Correct Response:")
    for x in range(0,11):
        # test to see if we get a 200/300 (multiple choices) response when entering correct input values
        i = random.randint(0,len(FromArray)) - 1
        j = random.randint(0,len(ToArray)) - 1
        # randomly pick a value from the array, array contents depends on what you pass into the cmd line
        FromInput = FromArray[i]
        ToInput = ToArray[j]
        generateURL(FromInput, ToInput)


def incorrectResponse():
    print("Incorrect Response:")
    # pass an incorrect value to see if the try/except statement gets triggered
    i = random.randint(0,len(FromArray)) - 1
    j = random.randint(0,len(ToArray)) - 1
    FromInput = FromArray[i] + "fefe"
    ToInput = ToArray[j]
    generateURL(FromInput, ToInput)

if __name__ == "__main__":
    correctResponse()
    incorrectResponse()
