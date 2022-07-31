from geoip import *

ip = input("Desired IP> ")

api = GeoIP(ip)
api.requestApi()
api.parseResponse()
api.buildResponse()
print(api.fetchResponse())