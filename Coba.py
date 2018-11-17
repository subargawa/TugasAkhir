import mysql.connector
import datetime
from prettytable import PrettyTable
import xlwt
import pandas as panda

book = xlwt.Workbook()


con_database = mysql.connector.connect(user="root", host="localhost", database="db_koprasi1")
cur_database = con_database.cursor(buffered=True)

cur_database.execute("SHOW TABLES")
tablesList= cur_database.fetchall()
b=0
for tables in tablesList:
    if len(tablesList)>b:
        tableName=tables[0]
        print(tableName)
        cur_database.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '%s'" %(tableName))
        colomnTable= cur_database.fetchall()
        b=b+1
        booksheet = book.add_sheet('tes'+str(b)+'')
        a= 0
        for columns in colomnTable:
            if len(colomnTable)>a:
                columnsName= (columns[3])
                print(columnsName)

                cur_database.execute("SELECT %s FROM  %s" % (columnsName, tableName))
                rowT = cur_database.fetchall()
                print("akawkakwka row", rowT)
                for dataRow in range(len(rowT)):
                    rowTable = rowT[a][0]
                    print("ini RT awkkawkaw",rowTable)
                    print("ini data row",dataRow)
                    booksheet.write(dataRow, a, columnsName)
                    a = a + 1
            else:
                pass

            # cur_database.execute("SELECT %s FROM  %s" % (columnsName, tableName))
            # rowT=cur_database.fetchall()
            # print("akawkakwka row",rowT)
            # x=1
            # y=0
            # for dataRow in rowT:
            #     rowTable=rowT[y][0]
            #     print("y=",y)
            #     print("ini RT awkkawkaw",rowTable)
            #     print("ini data row",dataRow)
            #     booksheet.write(10,10,rowTable)
            #     x = x + 1
            #     y=y+1

        book.save("D:ims.xls")
    else:
        pass
