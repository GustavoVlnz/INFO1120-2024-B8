import sqlite3
import pandas as pd
import data as filter 

conexion = sqlite3.connect("./plantilla_word/db_personas.db")
dataframe = pd.read_sql_query("SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios", conexion)
conexion.close()

print(dataframe)

def validar_entrada_numero():
    while True:
        try:
            n1 = int(input("Ingrese un número entre 0 y 48: "))
            if 0 <= n1 <= 48:
                print("El número está bien ingresado")
                return n1
            else:
                print("El número debe estar entre 0 y 48.")
        except ValueError:
            print("El valor ingresado no corresponde a un número.")

indice = validar_entrada_numero()

filter.singular_data_to_contract(dataframe, indice)

