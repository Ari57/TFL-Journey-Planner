import LocationNames
from LocationNames import FromArray, ToArray
from secret.keys import pk, sk
import requests
import sys

def startingLocation():
    print(" ")
    print("Starting Locations:")
    for i in range(0,len(FromArray)):
        print(FromArray[i])
    print(" ")
    FromInput = input("Please enter the name of your chosen starting location exactly as shown above: ")
    while FromInput == "Goodmayes, Barley Lane / Goodmayes Stn":
        FromInput = input("There's currently an issue with that location name, please select another: ")
    else:
        print("Chosen location: " + FromInput)
        return FromInput

def destinationLocation():
    print(" ")
    print("Destination Locations:")
    for i in range(0,len(ToArray)):
        print(ToArray[i])
    print(" ")
    ToInput = input("Please enter the name of your chosen destination location exactly as shown above: ")
    print("Chosen destination: " + ToInput)
    return ToInput

def generateURL(FromInput, ToInput):
    if FromInput == ToInput:
        print("The starting location cannot be the same as the destination")
        sys.exit(1)
    
    for i in range(0,len(FromArray)):
        for j in range(0,len(ToArray)):
            if FromInput == FromArray[i] and ToInput == ToArray[j]:
                url = "https://api.tfl.gov.uk/journey/journeyresults/"+FromInput+"/to/"+ToInput+"?app_id="+pk+"&app_key="+sk # enter your own keys in a seperate file and import them here

    try:
        response = requests.get(url)
        print(response)
        return response
    except NameError:
            print("One or both of your location names were incorrect")
            sys.exit(1)
        
def receiveResults(response):
    responseJson = response.json()

    for i in range(0,10):
        try:
            selectedRoute = responseJson["journeys"][i]["legs"]
            startTime = responseJson["journeys"][i]["startDateTime"]
            startPosition = startTime.find("T") + 1
            startResult = startTime[startPosition:]
            
            arrivalTime = responseJson["journeys"][i]["arrivalDateTime"]
            arrivalPosition = arrivalTime.find("T") + 1
            arrivalResult = arrivalTime[arrivalPosition:]
            print("-----------------")
            print("Starting time: " + startResult)
            print("Arrival time: " + arrivalResult)
            print("-----------------")
            for detail in selectedRoute:
                print("From", detail["departurePoint"]["commonName"])
                print(detail["instruction"]["detailed"])
                print("Arrive at", detail["arrivalPoint"]["commonName"])
        except IndexError:
            pass    

if __name__ == "__main__":
    receiveResults(generateURL(startingLocation(), destinationLocation()))
