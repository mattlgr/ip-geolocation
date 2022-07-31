from requests import get
from json import loads

class GeoIP:
    def __init__(self, target):
        self.target = target
    
    def requestApi(self):
        try:
            response = get(f"https://ipinfo.io/{self.target}/json")
            self.api_response = response
        except:
            self.api_response = None
    
    def parseResponse(self):
        if self.api_response == None:
            self.json_data = None
        else:
            self.json_data = loads(self.api_response.text) # Parses the json data into a usable format for the class.
    
    def buildResponse(self):
        if self.json_data == None:
            self.response = None
        else:
            self.response = "Response for: {}\nHostname: {}\nBasic Address: {}, {}, {}\nCoordinates: {}\nOrganisation: {}\nPostcode/Zip code: {}\nTimezone: {}".format(self.json_data["ip"], self.json_data["hostname"], self.json_data["country"], self.json_data["region"], self.json_data["city"], self.json_data["loc"], self.json_data["org"], self.json_data["postal"], self.json_data["timezone"]) # Bit of messy code due to F strings not supporting the formatting of the json data.

    def fetchResponse(self):
        return self.response