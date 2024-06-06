
import matplotlib.pyplot as plt

profesiones = ["Administrador de bases de datos", "Desarrollador de Software", "Ingeniero de sistemas", "Científico de datos", "Arquitecto de Software", "Desarrollador web", "Analista de datos", "Ingeniero de redes", "Especialista en Seguridad informática" ] 
dist_prof = [6.1 ,6.1 , 10.2, 10.2, 14.3 , 14.3 , 14.3, 20.4, 4.1]
plt.pie(dist_prof, labels=profesiones, autopct= '%1.1f%%')
plt.title( ' Distribución de profesiones ') 
plt.show()