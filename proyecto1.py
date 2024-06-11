#Importacion de librerias
import sqlite3 #Libreria util para trabajar con base de datos
import pandas as pd #Libreria util para manejar y hacer consultas a la base de datos
import data as filter  #filtro creado para unir la plantilla word con la base de datos y darle los indices necesarios

#Conexion y manejo de la base de datos
conexion = sqlite3.connect("./plantilla_word/db_personas.db") # crea la conexion con la base de datos para poder manejarla
dataframe = pd.read_sql_query("SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios", conexion) #consulta realizada para unir las tablas de la bd
conexion.close() #se cierra la conexion

print(dataframe)

#funcion para interactuar con el usuario
def validar_entrada_numero():
    while True: #genera un bucle infinito siempre y cuando los valores ingresados no sean validos
        try:
            n1 = int(input("Ingrese el primer numero entre 0 y 48: "))
            n2 = int(input("Ingrese el segundo numero entre 0 y 48: "))
            if 0 <= n1 <= 48 and 0 <= n2 <= 48: #verifica si los valores ingresados son validos
                if n1<=n2: #crea un if anidado para verificar si los valores estan dentro del rango y si n2 no es mayor a n1
                    print("Los numeros estan bien ingresados")
                    return n1, n2 #si estos cumplen las condiciones el while devuelve los valores de n1 y n2
                else:
                    print("n2 no puede ser mayor a n1") 
            else:
                print("Los número debe estar entre 0 y 48.") #de no cumplirse alguna de las dos condiciones entrega un mensaje y vuelve a pedirte el ingreso de datos
        except ValueError: #manejo del error principal que es el caso de que se ingrese un valor no numerico
            print("El valor ingresado no corresponde a un número.") 

n1,n2 = validar_entrada_numero() #a n1 y n2 se le asignan los valores dados por el usuario

for indice in range (n1,n2+1): #ocupa bucle for para que los valores dados por el usuario cumplan la funcion de un rango
    filter.singular_data_to_contract(dataframe,indice) # se llama al filtro para conectar dataframe con el indice
