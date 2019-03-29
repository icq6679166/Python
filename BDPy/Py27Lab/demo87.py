import sqlite3

connection1 = sqlite3.connect('demo87.sqlite')
print('open db success')
drop_sql = '''
DROP TABLE IF EXISTS EMPLOYEE;
'''
create_sql = '''
CREATE TABLE EMPLOYEE
(ID INT PRIMARY KEY,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
DEPT INT,
ADDRESS CHAR(50));
'''
connection1.execute(drop_sql)
connection1.execute(create_sql)
connection1.close()
