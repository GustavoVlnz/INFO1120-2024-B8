import matplotlib as mtp
import matplotlib.pyplot as plt

nacionalidad = ["Chilena", "Peruana", "Boliviana", "Argentina" ] 
emp_nacion = [14,14,11,10]
plt.bar(nacionalidad,emp_nacion, color = "blue")
plt.xlabel("Nacionalidad")
plt.ylabel("Cantidad de empleados")
plt.title("Conteo de profesionales por nacionalidad")
plt.xticks(rotation=45, ha='right')
plt.show()