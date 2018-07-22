import json
import requests
import googlemaps

#response_data = {}
address="Columbia University, New York, NY 10027, NY"
url="https://maps.googleapis.com/maps/api/geocode/json?address=%s" % (address)
try:
    response = requests.get(url)
    if not response.status_code == 200:
        print("HTTP error",response.status_code)
    else:
        try:
            response_data = response.json()
        except:
            print("Response not in valid JSON format")
except:
    print("Something went wrong with requests.get")
print(type(response_data))
print(response_data)
latitude = response_data['results'][0]['geometry']['location']['lat']
longitude = response_data['results'][0]['geometry']['location']['lng']
address = response_data['results'][0]['formatted_address']
print("Latitude :", latitude, "Longitude :",longitude)
print("Address :", address)

geocoder = googlemaps.geolocation()
print(geocoder)
