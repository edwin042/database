import json

# load city information
city_data = json.loads(open("city_list.json").read())

# Filter and write the Nepal coordinates to a file
data_file = "nepal_places" + ".txt"
f = open(data_file, "a")
for d in city_data:
    if d['country'] == 'NP':
        print_record = str(d['coord']['lat']) + "|" + str(d['coord']['lon']) + "\n"
        f.write(print_record)
f.close()
