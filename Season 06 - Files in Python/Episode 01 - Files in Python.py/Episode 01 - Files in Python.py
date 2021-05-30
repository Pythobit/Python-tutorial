# Files in Python

my_file = open('data.txt', 'r')
file_content = my_file.read()

my_file.close()
print(file_content)         # OUTPUT - Pythobit

"""
NOTICE : Here mode 'w' will erase any previous data in the 'data.txt' file and will overwrite it.
So, if you don't want to remove the contents, do not use the write mode.
"""
# if we want to ask user's name we'll ask it before writing into the file, as the file needs to be closed ASAP..
user_name = input('Enter your Name: ')

my_file_write = open('data.txt', 'w')
my_file_write.write(user_name)

my_file_write.close()


