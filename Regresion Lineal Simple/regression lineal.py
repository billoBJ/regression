# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:01:24 2019

@author: Billo
"""
#Como importar las librerias
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

#importar el dataset

dataset = pd.read_csv('Salary_Data.csv')

#variables independientes
x = dataset.iloc[:, :-1].values

#variables dependientes
y  = dataset.iloc[:,1].values

#dividir el dataset en entrenamiento y testing 
from sklearn.cross_validation import train_test_split
#1/3 quiere decir 1 de cada 3 se usara para test
x_train, x_test, y_train , y_test = train_test_split(x,y, test_size= 1/3, random_state =0) 

#crear modelo de regresion lineal 
#se utiliza el conjunto de entrenamiento 
from sklearn.linear_model import LinearRegression 
regression = LinearRegression()
regression.fit(x_train,y_train)

#predecir el conjunto de test
y_pred = regression.predict(x_test)


#visualizar los datos de entrenamiento 
plt.scatter(x_train, y_train, color="red")
plt.plot(x_train, regression.predict(x_train), color="blue")
plt.title("Sueldo vs Años de Experiencia (Conjunto de Entrenamiento)")
plt.xlabel("Años de Experiencia")
plt.ylabel("Sueldo (en $)")
plt.show()


#visualizar los datos de test 
plt.scatter(x_test, y_test, color="red")
plt.plot(x_train, regression.predict(x_train), color="blue")
plt.title("Sueldo vs Años de Experiencia (Conjunto de Testing)")
plt.xlabel("Años de Experiencia")
plt.ylabel("Sueldo (en $)")
plt.show()