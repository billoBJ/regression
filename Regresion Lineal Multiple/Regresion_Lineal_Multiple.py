# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:31:58 2019

@author: Billo
"""

# Regresion Limeal Multiple
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values


# Codificar datos categóricos String => numerico 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
X[:, 3] = labelencoder_x.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()

# Evitar la trampa de las variables ficticias
X = X[:, 1:]

# Dividir el data set en conjunto de entrenamiento y conjunto de testing
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train , y_test = train_test_split(X,y, test_size= 0.2, random_state =0)

#ajustar el modelo de regresion lineal multiple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression()

regression.fit(x_train, y_train)

#prediccion de los datos en el conjunto de test
y_pred = regression.predict(x_test)

#contruir el modelo optimo, utilizando eliminacion hacia atras
import statsmodels.formula.api as sm
# axis 0 = fila ,  1 = columna
X = np.append(arr = np.ones((50,1)).astype(int), values = X, axis = 1 )
SL = 0.05

#se evalua cada parametro, en esta instancia evaluamos todos los parametros 
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
regression_OLS = sm.OLS(endog = y, exog = X_opt.tolist()).fit()
regression_OLS.summary()
# se elimina la variable con el p-value mas alto, en este caso la columna 2 

#Luego de elimionar se vuelve a ajustar el modelo
X_opt = X[:, [0, 1, 3, 4, 5]]
regression_OLS = sm.OLS(endog = y, exog = X_opt.tolist()).fit()
regression_OLS.summary()

X_opt = X[:, [0, 3, 4, 5]]
regression_OLS = sm.OLS(endog = y, exog = X_opt.tolist()).fit()
regression_OLS.summary()

X_opt = X[:, [0, 3, 5]]
regression_OLS = sm.OLS(endog = y, exog = X_opt.tolist()).fit()
regression_OLS.summary()

X_opt = X[:, [0, 3]]
regression_OLS = sm.OLS(endog = y, exog = X_opt.tolist()).fit()
regression_OLS.summary()







 