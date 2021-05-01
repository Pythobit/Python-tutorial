# while loop
""" while loop works when we want to repeat something undefined times until the user tells the system to stop. """
is_learning = True
while is_learning:
    print('You\'re Learning..!')
# This above statement will run upto infinte times, as the value passed in the while loop will be True always..
# In order to stop the loop, we need make the variable make false.
is_learning = True
while is_learning:
    print('You\'re Learning..!')
    is_learning = False
# Above written 'is_learning = False', will make the condition inside the while loop as false,
# resulting in the termination of the while loop.
""" Now to make it more advance we can do like using user_input, as explained below. """
user_input = input('Are you still running (yes/no) : ')
while is_learning == user_input == "yes":
    print('You\'r still learning..!')
# Loop will continue only if the user will type 'yes', otherwise if the user types 'no', loop will terminate.
# here's an example
user_input = input('Do you wish to run the program (yes/no) : ')
while user_input  == "yes":
    print('We\'re Running the program../.\\')
    user_input = input('Do you wish to run the program (yes/no) : ')

print('We\'ve Stopped running')

""" Here's a Question for you """
# Create a Simple Text Menu
""" A menu is something that repeats over and over again until the user types something that makes the program terminate
 In our menu, the user will be able to choose from two options : 
 * if they type 'p', we will print "Hello"
 * if they type 'q', we will terminate the program
 
 How to start
 ** First, we'll ask the user for what they want to do the first, Do they want to print p or q"""
# Let's get started
# Ask the user to choose one of two options:
# if they type 'p', our program should print "Hello" and then ask the user again. Keep repeating this until...
# if they type 'q', our program should terminate.
user_input = input('Enter any on choice (p/q) : ')
# Let's begin by asking the user to type either 'p' or 'q'. You know how to do this using input()
# user_input = ...

while user_input != "q":
    if user_input == "p":
        print('Hello')

# Then, begin a while loop that runs for as long as the user doesn't type 'q'.
# Inside the loop, have an if statement that checks if the user typed 'p'.
#    If they did, print "Hello"
# Still inside the loop, ask the user again
# user_input = ...
