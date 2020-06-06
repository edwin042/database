import requests
import json
import uuid
from random_key import get_random_key

# file to write weather data to
data_file = "weather_data/" + str(uuid.uuid4()) + ".json"
f = open(data_file, "a")

# Pull data for each coordinates
file = open("nepal_places.txt", "r")
lines = file.readlines()
for line in lines:
    if line:
        lat = line.split("|")[0]
        lon = line.split("|")[1].rstrip()
        url = "http://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&appid=" + get_random_key()
        response = requests.get(url)
        f.write(response.text + "\n")
        print(response.text)
f.close()
