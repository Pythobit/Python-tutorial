# Python relative imports : Children

"""
File Structure

    utils
        common
            __init__.py
            file_operations.py
        __init__.py
        find.py
    app.py

"""
# from utils.common.file_operations import save_to_file  <-- Absolute Import
# from utils.find import find_in
# for relative import check find.py

print(__name__)     # OUTPUT - __main__
