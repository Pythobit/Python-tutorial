# CSV files in python

file = open('csv_data.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data = line.split(',')

    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].upper()
    degree = person_data[3].title()

    print(f'{name} is {age} years old, pursuing {degree} at {university}.')

# to join or add more names to it,
sample_csv_data = ':'.join(['pythobit', '21', 'amity', 'computer science'])
print(sample_csv_data)

