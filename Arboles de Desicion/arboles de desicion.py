# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:23:15 2020

@author: Billo
"""
# Regresión con Árboles de Decisión

# Cómo importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


#ajuste del modelo 
from sklearn.tree import DecisionTreeRegressor
regression = DecisionTreeRegressor(random_state = 0 )
regression.fit(X,y)

#prediccion 
y_pred = regression.predict(6.5)

#graficamos 
plt.scatter(X, y, color = "red")
plt.plot(X, regression.predict(X), color = "blue")
plt.title("Modelo de Regresión")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo (en $)")
plt.show()
