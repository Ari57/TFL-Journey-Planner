import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from JourneySteps import LocationChecking, generateURL, startingLocation, destinationLocation
from LocationNames import getLocationNames

def multipleLocations():
    # what happens when we pass in a value that has multiple locations
    getLocationNames("goodmayes", "romford")
    # Romford (London), Romford Station is one of these locations
    # I don't know of any others to test with, but they probably exist
    LocationChecking(generateURL(startingLocation(), destinationLocation()))

def oneLocation():
    # what happens when we pass in a value that has no extra locations
    getLocationNames("goodmayes", "canary wharf")
    LocationChecking(generateURL(startingLocation(), destinationLocation()))

    # the function has nothing to do, so it would just pass on to the receiveResults function, if we called it here

multipleLocations()
oneLocation()