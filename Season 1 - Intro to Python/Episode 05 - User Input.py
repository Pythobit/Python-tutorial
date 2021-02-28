# 5. User Input

name = "Pythobit"                               # Output
your_name = input("Enter your name: ")          # Enter your name: Pythoman
print(f"Hello {your_name}. My name is {name}")  # Hello Pythoman. My name is Pythobit
# Value given by the end-user must be string.
# Anything user types, python predicts as a string, whether it is a integer, or float.
# Multiplying an integer with a string will return integer no.s of those strings.
# To convert string into integer, we can use int(str_variable)

#e.g:
age = input("Enter your age: ")                     # Output
age_num = int(age)                                  # Enter your age: 20
print(f"You have lived for {age_num*12} months.")   # You have lived for 240 months.3
# Above shown is a Static method.
# For Dynamic method, use below method,
age = int(input("Enter your age: "))
print(f"You have lived for {age*12} months.")
# Program will wait for the input until the ENTER is Pressed.
