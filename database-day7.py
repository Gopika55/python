# Day 7- Python Database Connection Project which updates any one value in the table and select all the table data and print it.

import mysql.connector as sql          


database = sql.connect(host = 'localhost', user = 'root', passwd = 'ferrari458', database = 'schooldata')

cur = database.cursor()


cur.execute("update student set Eng_mark = 80 where Roll_no = 122")     
cur.execute("select * from student")        

for i in cur:
    print(i)

cur.close()
database.commit()       