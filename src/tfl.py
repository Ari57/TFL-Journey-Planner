import requests
from secret.keys import pk, sk
import sys

url = "https://api.tfl.gov.uk/Line/Mode/tube/Status?app_id="+pk+"&app_key="+sk # enter your own keys in a seperate file and import them here

response = requests.get(url)

responseJson = response.json()

for release in responseJson:
    if release["id"] == sys.argv[1]:
        #print(release["lineStatuses"][0]["statusSeverityDescription"])
        print(release["lineStatuses"][0]["reason"])