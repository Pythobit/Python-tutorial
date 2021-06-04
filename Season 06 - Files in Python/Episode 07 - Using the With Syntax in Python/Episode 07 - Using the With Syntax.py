# Using the with Syntax or Context Managers

"""
with Syntax or Context Managers are for automatically opening and closing of the files.
setup = opening the file
teardown = closing of the file
"""
import json

with open('friends_json.txt', 'r') as file:     # Notice change of synatax
    file_content = json.load(file)              # Indented line
                                                # file will be closed automatically.

print(file_content['friends'][0])


cars = [
    {
        'make': 'Ford', 'model': 'Fiesta'
    },
    {
        'make': 'Ford', 'model': 'Focus'
    }
]

with open('cars_json.txt', 'w') as file:
    json.dump(cars, file)


# Here we don't require a context manager as the string is directly uploading to a variable.
my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car)

# Next, we'll be creating our own Context Managers.
