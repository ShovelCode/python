# file location
  
import sqlite3  
 
conn = sqlite3.databs('databasename.db')  
  
print "Opened database successfully";  
conn.execute('''''CREATE TABLE Employees 
       (ID INT PRIMARY KEY NOT NULL, 
       NAME  TEXT    NOT NULL, 
       AGE INT NOT NULL, 
       ADDRESS CHAR(50), 
       SALARY REAL);''')  
print "Table is created";  
  
conn.close()  
