import json
import pandas as panda
import os

#Mendeklarasi fungsi "ExportDataToJson" dengan parameter "cur_database" dan "exportJson"
def ExportDataToJson(con_database,cur_database,exportJson):

    #Melakukan query menampilkan seluruh tabel yang ada pada database
    # dengan memanggil perintah ".execute" pada variabel "cur_database" dengan parameter query "SHOW TABLES"
    #Menyimpan seluruh result list tabel dari query pada variabel "tableList"
    # dengan memanggil perintah ".fetchall()" pada variabel "cur_database"
    cur_database.execute("SHOW TABLES")
    tableList = cur_database.fetchall()

    #Melakukan perulangan untuk mekanisme sistem dinamis dengan perulangan sebanyak jumlah row data
    # pada variabel "tableList" dan menyimpannya dalam variabel "tables"
    #Melakukan validasi dalam perulangan, dimana memvalidasi kondisi apabila jumlah panjang row pada variabel "tableList"
    # dengan menggunakan fungsi "len()" lebih besar dari nilai variabel "exportJson", maka akan dilanjutkan kedalam statement
    # apabila tidak memenuhi maka perulangan akan berlanjut ke value variabel "tables" berikutnya
    for tables in tableList:
        if len(tableList) > exportJson:

            #Mengambil nama tabel pada array 0 pada value variabel "tables" dan dimasukkan kedalam value variabel "tableName"
            #Mendeklarasikan directory untuk menyimpan file menggunakan "os.path.join" agar nama file yang akan dibuat pada
            # directory mengikuti nama tabel sesuai dengan value variabel "tableName"
            tableName = tables[0]
            locateFile = os.path.join("D:\Progect_Program\EntryFile\TA\Koprasi 2",""+ str(tableName) + ".json")

            #Membuat File Json Baru
            with open(locateFile, "w")as outfile:
                try:
                    data = json.load(outfile)
                except:
                    data = []

            #Meng-ekstrak file menjadi .json
            with open(locateFile, "r+") as jsonFile:
                writeJson = panda.read_sql("SELECT * FROM %s" % (tableName), con_database)
                writeJson.to_json(jsonFile, orient='records')
            exportJson = exportJson + 1

        else:
            pass
