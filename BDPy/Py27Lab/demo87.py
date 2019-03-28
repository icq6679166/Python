import  sqlite3

connection1 = sqlite3.connect('demo87.sqlite')
print('open db success')
connection1.close()