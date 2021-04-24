# Else Keyword with loop
cars = ['ok','ok','ok','faulty','ok','ok']

for status in cars:
    if status == 'faulty':
        print('Stopping the production line...')
        break
    print(f'This car is {status}.')
    print('Shipping new car to the Customer.')
# Above code is been used in this fragment
cars = ['ok','ok','ok','faulty','ok','ok']
all_successful = True
for status in cars:
    if status == 'faulty':
        print('Stopping the production line...')
        all_successful = False
        break
    print(f'This car is {status}.')
    print('Shipping new car to the Customer.')

if all_successful:  # this part of approach is known as NAIVE APPROACH, it involves a lot of coding, in order to not use that already built in programming language.
    print('All cars built succesfully, no faulty cars are found.')

# Instead of using 'if', we can use else here, with the same indentation as the for loop have, in order to write a understandable and clean code.
# Using else, will not require using all_successful variable, so new code comes out to be..,
cars = ['ok','ok','ok','ok','ok']

for status in cars:
    if status == 'faulty':
        print('Stopping the production line...')
        break
    print(f'This car is {status}.')
    print('Shipping new car to the Customer.')
else:
    print('All cars built succesfully, no faulty cars are found.')

""" -- OUTPUT -- 
# if a faulty car is in there..,
This car is ok.
Shipping new car to the Customer.
This car is ok.
Shipping new car to the Customer.
This car is ok.
Shipping new car to the Customer.
Stopping the production line...

# if there is no faulty car..,
This car is ok.
Shipping new car to the Customer.
This car is ok.
Shipping new car to the Customer.
This car is ok.
Shipping new car to the Customer.
This car is ok.
Shipping new car to the Customer.
This car is ok.
Shipping new car to the Customer.
All cars built succesfully, no faulty cars are found.
"""
