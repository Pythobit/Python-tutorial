# 4. Formatting Strings
# also known as 'f string'

age = 34
print(f"You are {age}")  # Output - You are 34

name = "Pythobit"
greet = f"How are you, {name}?"
print(greet)  # Output - How are you, Pythobit
# Changing name's value in continous doesn't change greet's value & the same line will print twice as above

name = "Pythobit"
greet = "How are you, {}?"
greet_new = greet.format(name)
print(greet_new)  # Output - How are you, Pythobit?

# Above statement will null & void this statement.
# We can print like this too below,
print(greet.format(name))
