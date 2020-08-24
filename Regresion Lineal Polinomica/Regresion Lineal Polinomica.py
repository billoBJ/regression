"""
Created on Sun Jan 12 21:36:13 2020

@author: Billo

REGRESION LINEAL POLINOMICA 
"""
#importar librerias 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#importar dataset 
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values 
Y = dataset.iloc[:,2:3].values

#como el conjunto de datos es pequenio (no uso enie por que no tengo c: ) 
#no dividiremos el conjunto de datos

#ajustar una regresion lineal \
from sklearn.linear_model import LinearRegression
Lin_reg = LinearRegression()
Lin_reg.fit(X,Y) #se realiza el ajuste  


#ajustar la regresion  polinomica con el dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg =  PolynomialFeatures(degree = 4 ) # por defecto degree = 2 (grado de la ecuacion polinomica)
x_poly = poly_reg.fit_transform(X) # se crea el conjunto de datos polinomial
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly,Y) #se crea el modelo con el conjunto de datos polinomial

#visualizacion de los datos del modelo lineal 
plt.scatter(X,Y,color="red") #dibujamos la nube de puntos, utilizando los datos
#dibuja la recta de la regresion lineal ajustada al modelo 
plt.plot(X,Lin_reg.predict(X), color="blue")
plt.title("Modelo de Regression Lineal")
plt.xlabel("Posicion del empleado")
plt.ylabel("Sueldo (en U$D)")
plt.show()

#Visualizacion de los datos del modelo polinomico
# se crea un vector rellenando los espacios  entre numeros discretos, sumando de a 0.1
X_grid = np.arange(min(X), max(X), 0.1)  
X_grid = X_grid.reshape(len(X_grid), 1)# se traspone el vector

plt.scatter(X,Y,color="red") #dibujamos la nube de puntos, utilizando los datos
#dibuja la recta de la regresion lineal ajustada al modelo 
plt.plot(X_grid,lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color="blue")
plt.title("Modelo de Regression Polinomico")
plt.xlabel("Posicion del empleado")
plt.ylabel("Sueldo (en U$D)")
plt.show()

# Predicción de nuestros modelos 
# Se ha añadido la sintaxis de doble corchete necesaria 
#para hacer la predicción en las últimas versiones de Python (3.7+)
Lin_reg.predict([[6.5]])
lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))