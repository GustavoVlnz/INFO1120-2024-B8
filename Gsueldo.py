
import matplotlib.pyplot as plt

profesiones = ["Administrador de bases de datos", "Desarrollador de Software", "Ingeniero de sistemas", "Científico de datos", "Arquitecto de Software", "Desarrollador web", "Analista de datos", "Ingeniero de redes", "Especialista en Seguridad informática" ] 
sueldo_prom = [1.5, 1.83,1.6,2,1.28,1.78,2.071,1.7,2]
plt.bar(profesiones,sueldo_prom, color = "purple")
plt.xlabel("Profesiones")
plt.ylabel("Sueldo promedio (millones CLP)")
plt.title("Promedio de Sueldo por Profesión")
plt.xticks(rotation=45, ha='right')
plt.show()