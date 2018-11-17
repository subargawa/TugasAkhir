import mysql.connector
import datetime
from prettytable import PrettyTable
import pandas as panda


con_database = mysql.connector.connect(user="root", host="localhost", database="db_koprasi1")
cur_database = con_database.cursor(buffered=True)

cur_database.execute("SHOW TABLES")
tablesList= cur_database.fetchall()
b=0
for tables in tablesList:
    if len(tablesList)>b:
        tableName=tables[0]
        # print(tableName)
        cur_database.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '%s'" %(tableName))
        colomnTable= cur_database.fetchall()
        print(colomnTable[2])

        a=panda.read_sql("SELECT * FROM %s"  %(tableName), con_database)
        a.to_excel('D:ims'+str(b)+'.xls')
        b= b+1