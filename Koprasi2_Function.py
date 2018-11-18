import json
import datetime

#Mendeklarasi fungsi "ExportDataToJson" dengan parameter "cur_database" dan "exportJson"
def ExportDataToJson(cur_database,exportJson):
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
    for tables in tableList:
        if len(tableList) > exportJson:
            tableName = tables[0]

            #Melakukan query dengan memanggil perintah ".execute" pada variabel "cur_database" dengan parameter
            # " "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '%s'" % (tableName)" yang artinya memilih semua
            # atribut skema terutama kolom pada tabel yang sesuai dengan nama tabel dari data yang diperoleh pada setiap perulangan
            # variabel "tableName"
            #Menyimpan seluruh list data skema dan kolom dari query pada variabel "tupleList"
            # dengan perintah ".fetchall()" pada variabel "cur_database"
            cur_database.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '%s'" % (tableName))
            tupleList = cur_database.fetchall()

            #Melakukan perulangan sebanyak jumlah row pada variabel "tupleList"untuk mekanisme dinamis pada setiap
            # row nama kolom yang diperoleh dan menyimpannya kedalam variabel "rowTuple"
            #Mengambil array ketiga dari variabel "rowTuple", dimana adalah nama colomn dari setiap tabel yang diperoleh
            # dan menyimpannya kedalam variabel "colomnTable"
            for rowTuple in tupleList:
                colomnTable = rowTuple[3]

                #Melakukan query dengan perintah ".excecute" pada variabel "cur_database" dengan parameter
                # "select %s from %s " % (colomnTable, tableName)" yang artinya melakukan select kolom pada value "colomnTable"
                # from value tabel "tableName" dimana value kolom dan tabel diperoleh secara dinamis
                # sesuai dengan jumlah list tabel dan jumlah list kolom pada setiap tabel
                #Menyimpan salah satu list data row pada setiap kolom dalam tabel pada variabel "rowData"
                # dengan menggunakan perintah ".fetchone()" pada variabel "cur_database"
                cur_database.execute("select %s from %s " % (colomnTable, tableName))
                rowData = cur_database.fetchone()

                #Mendeklarasikan variabel dictionary yang akan digunakan dalam melakukan perintah ".append" atau menulis
                # Json tanpa harus menghapus data Json yang lama agar membentuk suatu history
                #Membuka file pada directory disk yang dideklarasikan yaitu "menyusul" dengan hak akses "r" atau read
                # dan disimpan pada variabel "outfile" dengan perintah "as"
                #Melakukan sebuah validasi kondisi "try" dan "except", dimana apabila kondisi terpenuhi maka akan mendeklarasikan variabel "data"
                # dengan value melakukan perintah "json.load()" dengan parameter variabel "outfile".
                # kondisi yang apabila tidak terpenuhi maka mendeklarasikan variabel "data" dengan value dictionary
                list_data = []
                with open("D:\JSON.txt", "r", encoding='utf-8')as outfile:
                    try:
                        data = json.load(outfile)
                    except:
                        data = []

                #Mendeklarasikan variabel "new_entry" dengan value dictionary, dimana mendeklarasikan dictionary dengan format Json
                # yang mendeklarasikan object dengan nama value pada variabel "colomnTable", selanjutnya di-parsing menggunakan fungsi "str()" untuk merubah value menjadi
                # tipe data string, dan mendeklarasikan array atau isi data dari object dengan value dari variabel "rowData" yang diperoleh secara dinamis
                #Melakukan perintah ".append()" pada variabel list_data dengan parameter variabel new_entry yang nantinya
                # akan melakukan penulisan baru pada setiap data Json yang melakukan fungsi ".dump"
                new_entry = {"" + str(colomnTable) + "": rowData}
                list_data.append(new_entry)
                #Melakukan Open file pada drektory "menyusul" dengan hak akses "r+" atau read-write-execute kedalam variabel "outfile"
                #Melakukan perintah ".dump()" pada json atau menulis dengan parameter variabel "data" + "list_data" yang artinya
                # disatukan pada file dalam variabel "outfile" dan "indent=2" digunakan untuk membuat file json dapat mudah dibaca secara vertikal
                with open("D:\JSON.txt", "r+", encoding='utf-8') as outfile:
                    json.dump(data + list_data, outfile, indent=2)