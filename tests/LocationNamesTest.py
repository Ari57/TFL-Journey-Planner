import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from LocationNames import getLocationNames

def ValidInput():
    print("Valid Input:")
    # what happens when the function is given valid input
    getLocationNames("barking", "shenfield")
    getLocationNames("goodmayes", "canary wharf")
    getLocationNames("stratford", "paddington")
    getLocationNames("bank", "epping")
    print("Compiled successfully")
    # it compiles successfully, nothing is returned


def InvalidInput():
    print(" ")
    print("Invalid Input:")
    # what happens when we provide it with a number
    getLocationNames(1,1)

if __name__ == "__main__":
    ValidInput()
    InvalidInput()