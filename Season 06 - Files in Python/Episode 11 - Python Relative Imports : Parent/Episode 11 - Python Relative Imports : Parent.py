# Python relative imports : Parents

"""
if you want to import the parent, we need to use two dots instead of one as shown as below
"""
# `file_operations.py`
from ..find import NotFoundError
# ---^^ these two dots tells python to go the main import directory from where the project starts (i.e: utils)


