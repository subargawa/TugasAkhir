import mysql.connector
import os
import json
import time
from TugasAkhir.Dinas.Staging_function import identifikasiIndexData
from TugasAkhir.Dinas.Staging_function import transformDanMappingData
from TugasAkhir.Dinas.Staging_function import importDataToDatabase

con_database = mysql.connector.connect(user="root", host="localhost", database="db_stagging_dinas")
cur_database = con_database.cursor(buffered=True)

directoryFile=("D:\Progect_Program\EntryFile\TA\Koprasi 2")
listFile= os.listdir(directoryFile)
loop=True
while loop:
    print("========================================")
    print("===========Silahkan Pilih Menu==========")
    print("======[1] Identifikasi Index Data ======")
    print("======[2] Mapping File Ke Database =====")
    print("======[3] Import Data Ke Database ======")
    menu = int(input("Menu dipilih 1/2/3?:"))
    if menu ==1:
        print("========CEK DAN INPUT INDEX DATA========")
        for file in listFile:
            print("+++Nama Data..", file)
            locateFile = os.path.join(directoryFile, "" + str(file))
            filename = file[:-5]
            with open(locateFile, "r+") as jsonFile:
                filejson=json.load(jsonFile)
                print("+++Berikut Index File yang Tersedia...")
                print(filejson)
                time.sleep(2)

                #input data index
                lanjut=True
                while lanjut:
                    print("========================================")
                    index = input("Masukan Index Data: ")
                    lanjutkan= input("Lanjutkan Input Index Data? Y/N")

                    if lanjutkan == "y":
                        index = identifikasiIndexData(con_database,cur_database,filename,index)

                    elif lanjutkan== "n":
                        index = identifikasiIndexData(con_database, cur_database, filename, index)
                        lanjut=False

                    else:
                        index = identifikasiIndexData(con_database, cur_database, filename, index)
                        lanjut = False

    elif menu == 2:
        print("========MAPPING DATA MENUJU DATABASE========")
        for file in listFile:
            print("+++Nama Data..", file)
            locateFile = os.path.join(directoryFile, "" + str(file))
            filename = file[:-5]

            filename= transformDanMappingData(con_database,cur_database,filename,locateFile)


    elif menu == 3:
        print("==========IMPROT DATA MENUJU DATABASE==========")
        for file in listFile:
            print("+++Nama Data..", file)
            locateFile = os.path.join(directoryFile, "" + str(file))
            filename = file[:-5]
#function start Import Data
            cur_database.execute("select index_file from tb_data where nama_file='%s'" %
                                 (filename))
            indexF = cur_database.fetchone()
            indexFile = indexF[0].split(' ')[1:][:2]

            for column in indexFile:
                cur_database.execute("select * from tb_category")
                category=cur_database.fetchall()

                with open(locateFile, "r+") as jsonFile:
                    filejson = json.load(jsonFile)
                    for split in filejson:
                        splitJson= split[column].split(' ')

                        split = importDataToDatabase(con_database,cur_database,column,category,split)

