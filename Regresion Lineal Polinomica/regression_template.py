# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 20:15:03 2020

@author: Billo
"""
#plantilla de Regression 
#importar librerias 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#importar dataset 
dataset = pd.read_csv('')
X = dataset.iloc[:,1:2].values 
Y = dataset.iloc[:,2:3].values

# Dividir el data set en conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Escalado de variables //De ser necesario 
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


#ajustar la regresion con el dataset
#Crear el modelo de regresion


# Predicción de nuestros modelos 
y_pred = regression.predict(6.5)


#Visualizacion de los datos del modelo polinomico
# se crea un vector rellenando los espacios  entre numeros discretos, sumando de a 0.1
X_grid = np.arange(min(X), max(X), 0.1)  
X_grid = X_grid.reshape(len(X_grid), 1)# se traspone el vector

plt.scatter(X,Y,color="red") #dibujamos la nube de puntos, utilizando los datos
#dibuja la recta de la regresion lineal ajustada al modelo 
plt.plot(X_grid,regression.predict(X_grid), color="blue")
plt.title("Modelo de Regression")
plt.xlabel("")
plt.ylabel("")
plt.show()

