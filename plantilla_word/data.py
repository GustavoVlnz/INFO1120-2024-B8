import pandas as pd

import sqlite3
conexion=sqlite3.connect("db_personas.db")






df=pd.read_sql("db_personas.db",conexion)

totalsueldos=df["Salario"].sum 

query="Select * From Sueldo"
df=pd.read_sql_consulta(query,conexion)

conexion.close()
print(df.head())



def singular_data_to_contract(df: pd.DataFrame, index_row:int):
    sub_df = df.iloc[index_row]
    date = sub_df['Fecha']
    rol = sub_df['Rol']
    address = sub_df['Residencia']
    rut = sub_df['RUT']
    full_name = sub_df['nombre_completo']
    nationality = sub_df['Nacionalidad']
    birth_date = sub_df['Fecha de nacimiento']
    profession = sub_df['Profesion']
    salary = sub_df['Sueldo']
    example_contract(date, rol, address, rut, full_name, nationality, birth_date, profession, str(salary))

    







