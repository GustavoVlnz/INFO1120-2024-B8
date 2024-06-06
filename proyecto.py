import data as filter
import sqlite3
import pandas as pd 

conexion=sqlite3.connect("./plantilla_word/db_personas.db")
df=pd.read_sql_query("SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol=Salarios.id_salarios",conexion)

conexion.close()

filter.singular_data_to_contract(df,1)




