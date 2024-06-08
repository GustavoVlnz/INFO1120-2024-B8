import sqlite3
import pandas as pd
import data as filter 

conexion = sqlite3.connect("./plantilla_word/db_personas.db")
dataframe = pd.read_sql_query("SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios", conexion)
conexion.close()

#print(dataframe)

def validar_entrada_numero():
    while True:
        try:
            n1 = int(input("Ingrese el primer numero entre 0 y 48: "))
            n2 = int(input("Ingrese el segundo numero entre 0 y 48: "))
            if 0 <= n1 <= 48 and 0 <= n2 <= 48:
                if n1<=n2:
                    print("Los numeros estan bien ingresados")
                    return n1, n2
                else:
                    print("n2 no puede ser mayor a n1")
            else:
                print("Los número debe estar entre 0 y 48.")
        except ValueError:
            print("El valor ingresado no corresponde a un número.")

n1,n2 = validar_entrada_numero()

for indice in range (n1,n2+1):
    filter.singular_data_to_contract(dataframe,indice)
