# ip-geolocation
A simple python script to request, parse and build a response from the ipinfo.io API! This is just a simple practise as I am trying to sharpen my python skills.

This script uses https://ipinfo.io/ to build a simple ipinformation response from the api.

it parses this response:

```
{
  "ip": "***.**.***.***",
  "hostname": "********.**.***.***",
  "city": "East Cowes",
  "region": "England",
  "country": "GB",
  "loc": "50.753726107551, -1.2893486022949",
  "org": "****** *** ** Limited",
  "postal": "PO",
  "timezone": "Europe/London",
  "readme": "https://ipinfo.io/missingauth"
}
```

and prints this:

```
device@device MINGW64 ~/geo ip (master)
$ python main.py 
Desired IP> ***.**.***.***
Response for: ***.**.***.***
Hostname: ********.**.***.***
Basic Address: GB, England, East Cowes
Coordinates: 50.753726107551, -1.2893486022949 # Again not my house!
Organisation: ****** *** ** Limited
Postcode/Zip code: PO
Timezone: Europe/London

device@device MINGW64 ~/geo ip (master)
$
```
