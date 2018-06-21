def get_lat_lng(address_string):
    import json
    import requests
    url="https://maps.googleapis.com/maps/api/geocode/json?address=%s" % (address_string)
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
    latitude = response_data['results'][0]['geometry']['location']['lat']
    longitude = response_data['results'][0]['geometry']['location']['lng']
    address = response_data['results'][0]['formatted_address']
    #print("Latitude :", latitude, "Longitude :",longitude)
    #print("Address :", address)    
    return address, latitude, longitude

# OJO SOLO LA FUNCION!!!   
# Main Program #
address_string="Columbia University, New York, NY"

evalua_get_lat_lng = get_lat_lng(address_string)
print(evalua_get_lat_lng)
