# 3. Strings

# Values can be written inside between any quotes.
String = "Hello World"  # Strings can be written in double quotes
String = 'Hello World'  # Strings can be written in single quotes

print("Hello World")  # Output - Hello World

# Putting (\") will remove the meaning of quotes & known as 'escaping'
String = "He said \"you are amazing\" yesterday"

""" These are triple quotes and are 
used to introduce multiline strings
in it. """
""" White Spaces count too. """
""" There is no need to assign it to variable. """

name = "Pythobit"
greet = "Hello," + name
print(greet)  # Output - Hello, Pythobit

# Integers cannot be added in a string,
# But there's a way to add integers to string.
age = 34
string_age = str(age)
print("You are " + string_age)  # Output - You are 34

age="34"
print("You are " + age)  # Output - You are 34
