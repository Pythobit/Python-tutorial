# CSV to JSON Converter

# Please read the instructions carefully :
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Code starts here:
import json

json_list = []
csv_file = open('csv_file.txt', 'r')

for line in csv_file.readlines():
    club, city, country = line.strip().split(',')
    data = {
        'club': club,
        'city': city,
        'country': country
    }
    json_list.append(data)

csv_file.close()

json_file = open('json_file.txt', 'w')
json.dump(json_list, json_file)
json_file.close()
