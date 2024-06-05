import plantilla_word.data as filter
import sqlite3
import pandas as pd 


conexion=sqlite3.connect("./plantilla_word/db_personas.db")
df=pd.read_sql_query("SELECT  personas.nombre_completo,Salarios.rol FROM personas  INNER JOIN  Salarios on personas.id_rol=salarios.id_salarios ",conexion)



print(df)


conexion.close()
print(df.head())


filter.singular_data_to_contract


