import plantilla_word.data as filter
import sqlite3
import pandas as pd 


conexion=sqlite3.connect("./plantilla_word/db_personas.db")
df=pd.read_sql_query("SELECT * FROM Salarios",conexion)

totalsueldos=df["Sueldo"]


conexion.close()
print(df.head())


filter.singular_data_to_contract