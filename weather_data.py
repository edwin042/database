import requests
import json
from random_key import get_random_key

# load city information
json_data = open("city_list.json").read()
city_data = json.loads(json_data)

for d in city_data:
    resp = requests.get("http://api.openweathermap.org/data/2.5/weather?lat=" + str(d['coord']['lat']) + "&lon=" + str(d['coord']['lon']) + "&appid=" + get_random_key())
    json_data = json.loads(resp.text)
    print(json_data)
