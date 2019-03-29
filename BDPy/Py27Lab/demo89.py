import sqlite3
import time

connection1 = sqlite3.connect('demo87.sqlite')

employees = [{'NAME': 'Mark Ho', 'AGE': 43, 'DEPT': 1, 'ADDR': 'Taipei'},
             {'NAME': 'James Liu', 'AGE': 38, 'DEPT': 2, 'ADDR': 'Hsinchu'},
             {'NAME': 'Tim Chen', 'AGE': 33, 'DEPT': 3, 'ADDR': 'Taichung'}]

sql_dml = "INSERT INTO EMPLOYEE(NAME, AGE, DEPT, ADDRESS) VALUES (?,?,?,?)"
start_time = time.time()
for i in range(1000):
    for e in employees:
        connection1.execute(sql_dml, (e['NAME'], e['AGE'], e['DEPT'], e['ADDR']))
        connection1.commit()  # 19.42
    #connection1.commit()  # 6.437
#connection1.commit()#0.016
connection1.close()
print("---%s seconds---" % (time.time() - start_time))
