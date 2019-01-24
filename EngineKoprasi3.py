import mysql.connector
from TugasAkhir import Koprasi3_Function

con_database = mysql.connector.connect(user="root", host="localhost", database="db_koprasi3")
cur_database = con_database.cursor(buffered=True)

exportCSV=0
exportCSV= Koprasi3_Function.exportDataToCSV(con_database,cur_database,exportCSV)