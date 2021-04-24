# Break and Continue Keywords

cars = ['ok','ok','ok','faulty','ok','ok']
# Iterating over dictionaries
for status in cars:
    print(f'This car is {status}.')
""" -- OUTPUT -- 
This car is ok.
This car is ok.
This car is ok.
This car is faulty.
This car is ok.
This car is ok.
"""
""" as the serial goes on to like 'this car is ok, this car is ok', and suddenly it comes out to 
be 'this car is faulty.' , so production must be stopped, in order to get that car an inspection,
so the production needs to be stopped."""
# And here comes the break keyword.
for status in cars:
    if status == "faulty":
        print('Stopping the production line...')
        break
    print(f'This car is {status}.')
""" -- OUTPUT -- 
This car is ok.
This car is ok.
This car is ok.
Stopping the production line...
"""
# What here break does it that the break ends the loop, or we can say it terminates the loop.
print('\n')
for status in cars:
    if status == "faulty":
        print('Stopping the production line...')
        break
    print(f'This car is {status}.')
    print('Shipping the car to the customer...')
""" -- OUTPUT -- 
This car is ok.
Shipping the car to the customer...
This car is ok.
Shipping the car to the customer...
This car is ok.
Shipping the car to the customer...
Stopping the production line...
"""
# if you want to skip the faulty one, so the production doesn't stop,
# it can be done using continue keyword,
for status in cars:
    if status == 'faulty':
        print('Found FAULTY..! Skipping.../')
        continue
    print(f'This car is {status}')
    print('Shipping new car to the customer...')
""" -- OUTPUT -- 
This car is ok
Shipping new car to the customer...
This car is ok
Shipping new car to the customer...
This car is ok
Shipping new car to the customer...
Found FAULTY..! Skipping.../
This car is ok
Shipping new car to the customer...
This car is ok
Shipping new car to the customer...
"""

""" you won't understand the complete meaning of the use of break and continue immediately,
 but sooner you'll get it, as we move forward to the course, with the help of the examples,
 and mini projects, and after some more coding practices you'll understand more clearly..."""
