import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from JourneySteps import startingLocation
from LocationNames import getLocationNames

def validWord():
    # what happens when we pass a word in
    getLocationNames("goodmayes", "canary wharf")
    startingLocation()
    
    
def validLetter():
    print(" ")
    # what happens when we pass a letter in
    
    # in this situation, we received a KeyError as no stop points have "x" in their name
    # in the JourneySteps file, we raise an exception if a KeyError is detected
    getLocationNames("x", "w")
    startingLocation()

def incorrectStations():
    # what happens when a incorrect value is passed in
    print(" ")
    getLocationNames(True,False)
    startingLocation()

if __name__ == "__main__":
    validWord()
    validLetter()
    incorrectStations()