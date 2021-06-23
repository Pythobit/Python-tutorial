import sqlite3


class DatabaseConnection:
    def __init__(self, host):  # Initialisation of Object
        self.connection = None
        self.host = host

    def __enter__(self):    # Entering the body of Object
        self.connection =  sqlite3.connect('data.db')
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):  # Exiting the Body of Object
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()


"""
exc_type - Exception type
exc_val - Exception Value
exc_tb - Exception Trace-Back
"""

