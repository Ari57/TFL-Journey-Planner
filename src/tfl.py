import requests
from secret.keys import pk, sk
import sys

# ask the user where they want to go, search for those stations, take ics code, give directions
# url - journey/jr/ics/to/ics

fromLocation = "goodmayes"
toLocation = "canary wharf"

url = "https://api.tfl.gov.uk/journey/journeyresults/"+fromLocation+"/to/"+toLocation+"?app_id="+pk+"&app_key="+sk # enter your own keys in a seperate file and import them here

response = requests.get(url)

responseJson = response.json()

# TODO: find the length of whatever [0] is, iterate over it, pick up all stop names, display stop names, allow user to pick one, convert that to ICS code

test = responseJson["fromLocationDisambiguation"]["disambiguationOptions"][0]["place"]["icsCode"]
print(test)
test2 = responseJson["toLocationDisambiguation"]["disambiguationOptions"][1]["place"]["commonName"]
print(test2)