#Con matplotlib se puede hacer graficos matematicos cientificos y es una biblioteca

import numpy as np
import matplotlib.pyplot as plt 

#Dibujar una funcion seno
#Crear un ndarray de una dimensión, 100 elementos equiespacioandos desde o a 2*PI

x= np.linspace(0, 2*np.pi, 100)
y= np.sin(x)

#Usar matplotlib

plt.figure(figsize=(8,4))
plt.title("Mi primer grafico cientifico en programación :D")
plt.xlabel("x")
plt.ylabel("Seno de x")
plt.grid(True)
plt.plot(x,y)
plt.show()
