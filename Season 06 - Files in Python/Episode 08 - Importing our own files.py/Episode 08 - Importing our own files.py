# Importing our own files in Python

# there are two ways to import the file_operations file
import file_operations

file_operations.save_to_file('Rolf', 'data.txt')
file_operations.read_file('data.txt')

# Another Way
from file_operations import save_to_file, read_file     # This will be available globally entire code

save_to_file('Rolf', 'data.txt')
"""
for larger apps, we need to make a directory as utils/utility and file_operations.py is part of utils   
"""
# So, it should be
import utils.file_operations

utils.file_operations.save_to_file('Rolf', 'data.txt')
utils.file_operations.read_file('data.txt')

# Another Way
from utils.file_operations import save_to_file, read_file     # This will be available globally entire code

save_to_file('Rolf', 'data.txt')
read_file('data.txt')

"""
We need to tell the python that `util` is a package, so in order to tell that, we need to make a file `__init__.py`, 
no need to write anything in it, it is a compliance for python older versions.
"""
