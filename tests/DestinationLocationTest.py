import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from JourneySteps import destinationLocation
from LocationNames import getLocationNames

def Word():
    # what happens when we pass a word in
    getLocationNames("goodmayes", "canary wharf")
    destinationLocation()
    getLocationNames("mile", "london")
    destinationLocation()
    getLocationNames("woodford", "leyton")
    destinationLocation()
    getLocationNames("blue", "green")
    destinationLocation()
    getLocationNames("chocolate", "ice cream") # KeyError as no stop points have "chocolate" or "ice cream" in their name
                                                # in the JourneySteps.py file, we have a try statement to catch any KeyErrors found while executing the getLocationNames function
  
    
    
def Letter():
    print(" ")
    # what happens when we pass a letter in
    
    # in this situation, we received a KeyError as no stop points have "x" in their name
    # in the JourneySteps file, we raise an exception if a KeyError is detected
    getLocationNames("x", "w")
    destinationLocation()

def IncorrectDataType():
    # what happens when a incorrect value is passed in
    print(" ")
    getLocationNames(True,False)
    destinationLocation()

if __name__ == "__main__":
    Word()
    Letter()
    IncorrectDataType()