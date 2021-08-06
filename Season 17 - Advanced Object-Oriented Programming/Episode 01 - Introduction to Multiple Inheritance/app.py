from admin import Admin
from database import Database


a = Admin('rolf', '1244', 3)
a.save()

print(Database.find(lambda x: x['username'] == 'rolf'))
