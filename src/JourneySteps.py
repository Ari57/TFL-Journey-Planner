from LocationNames import getLocationNames, FromArray, ToArray
from secret.keys import pk, sk
import requests
import sys

# https://stackoverflow.com/questions/50405112/how-to-deal-with-the-slash-and-2f-in-python

def startingLocation():
    print(" ")
    print("Starting Locations:")
    for i in range(0,len(FromArray)):
        print(FromArray[i])
    print(" ")
    FromInput = input("Please enter the name of your chosen starting location exactly as shown above: ")
    # while FromInput == "Goodmayes, Barley Lane / Goodmayes Stn":
    #     FromInput = input("There's currently an issue with that location name, please select another: ")
    # else:
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
        if FromInput == FromArray[i]:
            break

    for i in range(0,len(ToArray)):
            if ToInput == ToArray[i]:
                url = "https://api.tfl.gov.uk/journey/journeyresults/"+FromInput+"/to/"+ToInput+"?app_id="+pk+"&app_key="+sk # enter your own keys in a seperate file and import them here
                break
    try:
        response = requests.get(url)
        return response
    except NameError:
            print("One or both of your location names were incorrect")
            sys.exit(1)
        
def LocationChecking(response):
    responseJson = response.json()

    # sometimes, one of the locations a user picks, has multiple locations
    # https://api.tfl.gov.uk/journey/journeyresults/Barking and Dagenham, Chelmer Wines, Barking/to/Ealing, Greengate?app_id&app_key
    # above is a valid request, but it returns results similar to LocationNames.py file

    # if this key exists, then the wrong results have been returned
    # let the user know that the location they entered was wrong
    # and provide a list of more specific locations

    try:
        if responseJson["fromLocationDisambiguation"]:
            FromArray2 = []
            for i in range(0,71):
                try:
                    FromResponse = responseJson["fromLocationDisambiguation"]["disambiguationOptions"][i]["place"]["commonName"]
                    FromArray2.append(FromResponse)
                except IndexError:
                    break
            
            print("The locations you entered returned too many results, pick one of the locations below:")
            print(" ")
            for i in range(0,len(FromArray2)):
                print(FromArray2[i])
            sys.exit(1)
    except KeyError:
        pass
    
    try:
        if responseJson["toLocationDisambiguation"]:
            ToArray2 = []
            for i in range(0,71):
                try:
                    ToResponse = responseJson["toLocationDisambiguation"]["disambiguationOptions"][i]["place"]["commonName"]
                    ToArray2.append(ToResponse)
                except IndexError:
                    break
            print("The locations you entered returned too many results, pick one of the locations below:")
            print(" ")
            
            for i in range(0,len(ToArray2)):
                print(ToArray2[i])
            sys.exit(1)
    except KeyError:
        pass

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
            break    

if __name__ == "__main__":
    try:
        getLocationNames(sys.argv[1], sys.argv[2])
    except KeyError:
        print("Incorrect location names given")
        sys.exit(1)
    
    receiveResults(LocationChecking(generateURL(startingLocation(), destinationLocation(),)))
