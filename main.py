from geoip import *
import sys

ip = input("Desired IP> ")

api = GeoIP(ip)

if api.validate_ipv4() == None:
    print("Invalid IP given!")
    sys.exit(0)

api.requestApi()
api.parseResponse()
api.buildResponse()
print(api.fetchResponse())
