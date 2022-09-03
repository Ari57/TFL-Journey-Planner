import requests
from secret.keys import pk, sk
import sys

# this takes the starting/destination location from the user
# and returns a list of all stop points matching the location

fromLocation = sys.argv[1]
toLocation = sys.argv[2]

url = "https://api.tfl.gov.uk/journey/journeyresults/"+fromLocation+"/to/"+toLocation+"?app_id="+pk+"&app_key="+sk # enter your own keys in a seperate file and import them here

response = requests.get(url)

responseJson = response.json()

FromArray = []
ToArray = []

for i in range(0,71):
    try:
        fromResponse = responseJson["fromLocationDisambiguation"]["disambiguationOptions"][i]["place"]["commonName"]
        ToResponse = responseJson["toLocationDisambiguation"]["disambiguationOptions"][i]["place"]["commonName"]
        FromArray.append(fromResponse)
        ToArray.append(ToResponse)
    except IndexError:
        pass

# TODO: find the length of whatever [0] is, iterate over it, pick up all stop names, display stop names, allow user to pick one, convert that to ICS code
