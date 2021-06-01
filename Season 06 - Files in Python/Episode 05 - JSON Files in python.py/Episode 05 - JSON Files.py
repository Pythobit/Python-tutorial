# JSON (Javascript Object Notation) files in Python

import json

file = open('friends_json.txt', 'r')
file_content = json.load(file)
file.close()

print(file_content['friends'][0])


cars = [
    {
        'make': 'Ford', 'model': 'Fiesta'
    },
    {
        'make': 'Ford', 'model': 'Focus'
    }
]

file = open('cars_json.txt', 'w')
json.dump(cars, file)
file.close()


my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car)

