from geopy.geocoders import Nominatim
from tkinter import *

geolocator = Nominatim(user_agent="mukhammadjonovxamidullo@gmail.com")
location = geolocator.geocode("Turin")

print("The latitude: ", location.latitude)
print("The longitude: ", location.longitude)

location = geolocator.reverse("45.0677551, 7.6824892")

address = location.raw['address']

print(address)