#taller numpy.

import numpy as np 
import matplotlib as mp

#Crear um arreglo n dimensional a partir de una lista

a=np.array([[1,5], [7,9]])
b=np.array([[2,0], [1,3]])

#Sacar el producto punto entre a y b

c= np.dot(a,b)
print(c)

#Solción de un sistema de ecuaciones expersadas por un matriz com mu,py

matrizSolucion= np.array([5,17])

m= np.linalg.solve(a, matrizSolucion)

print(m)
