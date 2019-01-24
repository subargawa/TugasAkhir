import mysql.connector
from TugasAkhir.Koprasi2_Function import ExportDataToJson

#Koneksikan database berupa "user","host" dan "database" pada db_koprasi2 dimana adalah database koprasi kedua
# dan memasukkannya kedalam variabel "con_database"
#Memanggil perintah cursor pada variabel "con_database" dan menyimpannya dalam variabel "cur_database"
con_database = mysql.connector.connect(user="root", host="localhost", database="db_koprasi2")
cur_database = con_database.cursor(buffered=True)

#Deklarasikan variabel "exportJson" dengan nilai awal 0 yang nantinya akan digunakan oleh engine "Koprasi2_Function" sebagai perulangan
#Memanggil fungsi "ExportDataToJson" pada engine "Koprasi2_Function" dengan parameter variabel "cur_database" dan "exportJson"
exportJson = 0
exportJson = ExportDataToJson(con_database,cur_database,exportJson)