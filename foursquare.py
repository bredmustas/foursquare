import httplib2
import json


foursquare_client_id = "3LCXP3GIU1TGAVGHOD4KOMNOQI1WDV0LHDKLJIXD5ETH0K3V"
foursquare_client_secret = "ZEYGQY5YETITWIY3MYVKBXUFL03J4FSM3RIBOR2XOSE2YQU5"

def getGeocodeLocation(inputString):
    # Use Google Maps to convert a location into Latitute/Longitute coordinates
    # FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY
    google_api_key = "AIzaSyB6WqehMP1XVNWekT_adIZx67lL_m6l1F8"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)

def findARestaurant(mealType, location):
    locationCord = getGeocodeLocation(location)
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret, locationCord[0], locationCord[1], mealType))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    for x in range(len(result)):
        restaurant = result['response']['venues'][x]
        venue_id = restaurant['id']
        restaurant_name = restaurant['name']
        restaurant_address = restaurant['location']['address']
        print("Id " + venue_id)
        print("Name " + restaurant_name)
        print("Address " + restaurant_address)
        print("")

if __name__ == "__main__":
    findARestaurant("Pizza", "Berlin, Germany")
