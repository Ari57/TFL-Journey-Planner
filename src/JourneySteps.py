import LocationNames
from LocationNames import FromArray, ToArray
from secret.keys import pk, sk
import requests
import sys

print(" ")
print("Starting Locations:")
for i in range(0,len(FromArray)):
    print(FromArray[i])
print(" ")
FromInput = input("Please enter the name of your chosen starting location exactly as shown above:")
print("Chosen location: " + FromInput)

print(" ")
print("Destination Locations:")
for i in range(0,len(ToArray)):
    print(ToArray[i])
print(" ")
ToInput = input("Please enter the name of your chosen destination location exactly as shown above:")
print("Chosen destination: " + ToInput)
print(" ")


for i in range(0,len(FromArray)):
    for j in range(0,len(ToArray)):
        if FromInput == FromArray[i] and ToInput == ToArray[j]:
            url = "https://api.tfl.gov.uk/journey/journeyresults/"+FromInput+"/to/"+ToInput+"?app_id="+pk+"&app_key="+sk # enter your own keys in a seperate file and import them here

try:
    response = requests.get(url)
except NameError:
        print("One or both of your location names were incorrect")
        sys.exit(1)

responseJson = response.json()

for i in range(0,50):
    try:
        selectedRoute = responseJson["journeys"][i]["legs"]
        print(" ")
        for detail in selectedRoute:
            print("From", detail["departurePoint"]["commonName"])
            print(detail["instruction"]["detailed"])
            print("Arrive at", detail["arrivalPoint"]["commonName"])
    except IndexError:
           pass


