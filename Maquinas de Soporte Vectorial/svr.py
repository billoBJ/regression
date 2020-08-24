# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:37:24 2020

@author: Billo
"""
#SVR

# Importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


from sklearn.preprocessing import StandardScaler 
sc_X = StandardScaler()
sc_y = StandardScaler()

X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

#ajustar la regresion con el dataset
from sklearn.svm import SVR
regression = SVR(kernel = 'rbf')
regression.fit(X,y)

y_pred = sc_y.inverse_transform(regression.predict(sc_X.transform(np.array([[6.5]]))))


# Visualización de los resultados del SVR
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = "red")
plt.plot(X_grid, regression.predict(X_grid), color = "blue")
plt.title("Modelo de Regresión (SVR)")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo (en $)")
plt.show()
