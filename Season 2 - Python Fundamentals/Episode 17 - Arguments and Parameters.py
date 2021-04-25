# Arguments and Parameters
""" Arguments : Value that you pass in the function..
    Parameters : Variable that accepts value inside the function..  """
""" These help make our functions more generic, so we can use them with multiple pieces of data.. """
car = {
    'make': 'Ford',
    'model': 'Fiesta',
    'mileage': 23000,
    'fuel_consumed': 460
}
mpg = car['mileage'] / car['fuel_consumed']
name = f"{car['make']} {car['model']}"
print(f'{name} does {mpg} miles per gallon.')       # OUTPUT - Ford Fiesta does 50.0 miles per gallon.

# We can also do this using function.
def calculate_mpg():
    car = {
        'make': 'Ford',
        'model': 'Fiesta',
        'mileage': 23000,
        'fuel_consumed': 460
    }
    mpg = car['mileage'] / car['fuel_consumed']
    name = f"{car['make']} {car['model']}"
    print(f'{name} does {mpg} miles per gallon.')
calculate_mpg()                                    # OUTPUT - Ford Fiesta does 50.0 miles per gallon.
# Aside from this, we can use arguments and parameters..,
car = {
    'make': 'Ford',
    'model': 'Fiesta',
    'mileage': 23000,
    'fuel_consumed': 460
}

def calculate_mpg(car_to_calculate):
    mpg = car_to_calculate['mileage'] / car_to_calculate['fuel_consumed']
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f'{name} does {mpg} miles per gallon.')
# calculate_mpg()

# what this argument does is that it passes the variable's parameters to the functions call, as shown below..,
calculate_mpg({
    'make': 'Ford',
    'model': 'Fiesta',
    'mileage': 23000,
    'fuel_consumed': 460
})

# Example
cars = [
    {'make': 'Ford', 'model': 'Fiesta', 'mileage': 23000, 'fuel_consumed': 460},
    {'make': 'Ford', 'model': 'Focus', 'mileage': 17000, 'fuel_consumed': 350},
    {'make': 'Mazda', 'model': 'MX-5', 'mileage': 49000, 'fuel_consumed': 900},
    {'make': 'Mini', 'model': 'Cooper', 'mileage': 31000, 'fuel_consumed': 235},
]
def calculate_mpg(car):
    mpg = car['mileage'] / car['fuel_consumed']
    name = f'{car["model"]}'
    print(f'{name} does {mpg} miles per gallon.')

for car in cars:
    calculate_mpg(car)

""" -- OUTPUT -- 
Fiesta does 50.0 miles per gallon.
Focus does 48.57142857142857 miles per gallon.
MX-5 does 54.44444444444444 miles per gallon.
Cooper does 131.91489361702128 miles per gallon.
"""
