import mysql.connector
import datetime
from prettytable import PrettyTable
import pandas as panda

con_database = mysql.connector.connect(user="root", host="localhost", database="db_koprasi1")
cur_database = con_database.cursor(buffered=True)


def exportDataToExcel(con_database, exportExcel):
    #Menampilkan Seluruh Table
    cur_database.execute("SHOW TABLES")
    tablesList= cur_database.fetchall()
    ##memberikan nilai awal variabel untuk dilakukannya +1 pada setiap perulangan selanjutnya

    for tables in tablesList:
        if len(tablesList)>exportExcel:
            tableName=tables[0]
            # print(tableName)
            cur_database.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '%s'" %(tableName))
            colomnTable= cur_database.fetchall()
            print(colomnTable[2])

            a=panda.read_sql("SELECT * FROM %s"  %(tableName), con_database)
            a.to_excel('D:ims'+str(exportExcel)+'.xls')
            exportExcel= exportExcel+1

        else:
            pass