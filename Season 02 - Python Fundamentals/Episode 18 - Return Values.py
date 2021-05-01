# Return Values

cars = [
    {'make': 'Ford', 'model': 'Fiesta', 'mileage': 23000, 'fuel_consumed': 460},
    {'make': 'Ford', 'model': 'Focus', 'mileage': 17000, 'fuel_consumed': 350},
    {'make': 'Mazda', 'model': 'MX-5', 'mileage': 49000, 'fuel_consumed': 900},
    {'make': 'Mini', 'model': 'Cooper', 'mileage': 31000, 'fuel_consumed': 235},
]
def calculate_mpg(car):
    mpg = car['mileage'] / car['fuel_consumed']
    return mpg
# what return does is that it return the value to the function.
for car in cars:
    mpg = calculate_mpg(car)

# Ex.:
def calculate_mpg(car):
    mpg = car['mileage'] / car['fuel_consumed']
    return mpg

def car_name(car):
    name = f'{car["make"]} {car["model"]}'
    return name

def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)
    print(f'{name} does {mpg} miles per gallon.')

for car in cars:
    mpg = calculate_mpg(car)

# if we won't return any value, so the default value for the return will be None.
# Return None, if you want it as explicit value..,

# Example..
def divide(x, y):
    if y == 0:
        return "You've tried to divide by Zero.."
    else:
        return x / y
""" Having two return statements in a function won't work, only the first return statement will run & then terminates..
but, both the returns can run, if we use else keyword.."""
print(divide(10, 2))        # OUTPUT - 5.0
print(divide(6, 0))         # OUTPUT - You've tried to divide by Zero..
