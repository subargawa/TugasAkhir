import pandas as panda
import os

def exportDataToCSV(con_database, cur_database, exportCSV):
    cur_database.execute("SHOW TABLES")
    tableList =cur_database.fetchall()
    for tables in tableList:
        if len(tableList)>exportCSV:
            tableName=tables[0]

            # Meng-ekstrak file menjadi .csv
            locateFile = os.path.join("D:\Progect_Program\EntryFile\TA\Koprasi 3", ""+ str(tableName) + ".csv")
            with open (locateFile,"r+") as csvFile:
                writeCSV= panda.read_sql("SELECT * FROM %s"  %(tableName), con_database)
                writeCSV.to_csv(csvFile, index=False)
            exportCSV = exportCSV + 1
        else:
            pass

