from LocationNames import getLocationNames, FromArray, ToArray
from secret.keys import pk, sk
from secret.dbdetails import conn
import requests
import sys
import psycopg2

# https://stackoverflow.com/questions/50405112/how-to-deal-with-the-slash-and-2f-in-python

# CTRL K, CTRL 0 to collapse everything



def startingLocation():
    if FromArray:
        print("Starting Locations:\n")
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
    if ToArray:
        print("Destination Locations:\n")
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
                cursor = conn.cursor()
                cursor.execute("INSERT INTO journeylocations (start, dest) VALUES(%s, %s)", (FromInput, ToInput)) # need some form of protection here
                 
                
                break
    try:
        response = requests.get(url) # type: ignore | raises a "reportUnboundVariable" problem, (as it should)
        return response
    except NameError:
            print("One or both of your location names were incorrect")
            sys.exit(1)

def LocationChecking(response):
    responseJson = response.json()
   
    # sometimes, one of the locations a user picks, has multiple locations
    # https://api.tfl.gov.uk/journey/journeyresults/Barking and Dagenham, Chelmer Wines, Barking/to/Ealing, Greengate
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
    
    return response

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

        return response
        
def TrainStatus(response):
    responseJson = response.json()
    lineArray = []

    for i in range(0,10):
        for j in range(0,10):
            try:
                result = responseJson["journeys"][i]["legs"][j]["routeOptions"][0]["lineIdentifier"]["id"]
                if result in lineArray: # it's possible to get duplicates of the lines
                    pass
                else:
                    lineArray.append(result)
            except (IndexError, KeyError) as error:
                pass

    print(" ")
    # for loop, go through array, make a request each time and print status 
    for trainLine in lineArray:
        urlStatus = "https://api.tfl.gov.uk/Line/"+trainLine+"/Status?detail=true&app_id="+pk+"&app_key="+sk
        statusResponse = requests.get(urlStatus)
        statusResponseJson = statusResponse.json()
        lineName = statusResponseJson[0]["name"]
        lineStatus = statusResponseJson[0]["lineStatuses"][0]["statusSeverityDescription"]
        try:
            reason = statusResponseJson[0]["lineStatuses"][0]["reason"]
        except KeyError:
            reason = "" # need to reset "reason", otherwise anything without the "reason" key, will use the last value that "reason" was set to
            pass
        if reason:
            print(lineName, "-", lineStatus, "-", reason)
        else:
            print(lineName, "-", lineStatus)
        print(" ")

def GoogleMaps():
    cursor = conn.cursor()
    cursor.execute("SELECT * from journeylocations;")
    record = cursor.fetchall()
    for row in record:
        start = row[0]
        dest = row[1]
    print("Starting: "  + start) # type: ignore | it thinks it's unbound, it's not
    print("Destination: " + dest) # type: ignore
    cursor.execute("delete from journeylocations;") #  can delete once we've printed it, for now
    conn.close()

    
   
if __name__ == "__main__":
    try:
        getLocationNames(sys.argv[1], sys.argv[2])
    except KeyError:
        print("Incorrect location names given")
        sys.exit(1)

        # use double quotes to search for multi word locations
        # e.g. "North Greenwich"
    
    TrainStatus(receiveResults(LocationChecking(generateURL(startingLocation(), destinationLocation()))))
    GoogleMaps()