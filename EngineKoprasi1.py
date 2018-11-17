import mysql.connector
import datetime
from prettytable import PrettyTable
import pandas as panda
from MDI.TugasAkhir import Koprasi1_Function

con_database = mysql.connector.connect(user="root", host="localhost", database="db_koprasi1")
cur_database = con_database.cursor(buffered=True)

exportExcel= Koprasi1_Function.exportDataToExcel(con_database, exportExcel)