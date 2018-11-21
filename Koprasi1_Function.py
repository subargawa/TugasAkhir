import datetime
import pandas as panda

def exportDataToExcel(con_database, cur_database, exportExcel):
    #Menampilkan Seluruh Table
    cur_database.execute("SHOW TABLES")
    tablesList= cur_database.fetchall()
    ##memberikan nilai awal variabel untuk dilakukannya +1 pada setiap perulangan selanjutnya

    for tables in tablesList:
        if len(tablesList)>exportExcel:
            tableName=tables[0]

            writeExcel=panda.read_sql("SELECT * FROM %s"  %(tableName), con_database)
            writeExcel.to_excel('D:ims'+str(exportExcel)+'.xls')
            exportExcel= exportExcel+1

        else:
            pass
