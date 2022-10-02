import requests
import sys
from secret.keys import pk, sk

FromArray = []
ToArray = []

def getLocationNames(fromLocation, toLocation):
    FromArray.clear() # if the function is called more than once (at the same time), we need to reset the array
    ToArray.clear()
    
    # if the user tries to pass in a int (for example), it can't concat to a string
    # this raises a TypeError

    try:
        url = "https://api.tfl.gov.uk/journey/journeyresults/"+fromLocation+"/to/"+toLocation+"?app_id="+pk+"&app_key="+sk # enter your own keys in a seperate file and import them here
    except TypeError:
            print("Unable to concat",type(fromLocation), "or",type(toLocation),"to a string. Please provide a string instead.")
            sys.exit(1)

    response = requests.get(url)

    responseJson = response.json()

    # we run it an unknown number of times as we don't know how many results we could receive
    # once it receives an IndexError, it breaks
    
    for i in range(0,71):
        try:
            fromResponse = responseJson["fromLocationDisambiguation"]["disambiguationOptions"][i]["place"]["commonName"]
            ToResponse = responseJson["toLocationDisambiguation"]["disambiguationOptions"][i]["place"]["commonName"]
            FromArray.append(fromResponse)
            ToArray.append(ToResponse)
        except IndexError:
            break

    return response

