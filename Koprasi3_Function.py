import pandas as panda
import os

def exportDataToCSV(con_database, cur_database, exportCSV):


    cur_database.execute("SHOW TABLES")
    tableList =cur_database.fetchall()
    for tables in tableList:
        if len(tableList)>exportCSV:
            tableName=tables[0]
            print("=====================================")
            print("nama tabel adalah",tableName)
            cur_database.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '%s'" % (tableName))
            tupleList= cur_database.fetchall()
            locateFile = os.path.join("D:\TA\Koprasi 3", "CSV" + str(exportCSV) + ".csv")
            with open (locateFile,"r+") as csvFile:
                writeCSV= panda.read_sql("SELECT * FROM %s"  %(tableName), con_database)
                writeCSV.to_csv(csvFile, index=False)
                print(exportCSV)
            exportCSV = exportCSV + 1
        else:
            pass

