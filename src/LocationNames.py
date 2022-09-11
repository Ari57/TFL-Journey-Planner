import requests
import sys
from secret.keys import pk, sk

# this takes the starting/destination location from the user

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
    except KeyError:
        print("Unable to find results under the start/destination location")
        sys.exit(1)
    
    try:
        FromArray.append(fromResponse)
        ToArray.append(ToResponse)
    except IndexError:
        pass

if __name__ == "__main__":
    pass

