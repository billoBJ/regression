# Regresion Polinomica

# Importar el dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[,2:3]

#al ser un dataset pequenio no es eficiente realizar la division
# por test  y train

#ajustar el modelo de de regresion lineal
lin_reg = lm(formula = Salary ~ . , data = dataset)

#Ajustamos el modelo de regresion Polinomico
dataset$Level2 = dataset$Level^2 #aniadimos las columnas
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
lin_pol = lm(formula = Salary ~ . , data = dataset )

#Visualizacion del modelo Lineal
library(ggplot2)
ggplot() +
  geom_point(aes(x= dataset$Level , y= dataset$Salary ), color = "red") + #grafica de puntos 
  geom_line(aes(x = dataset$Level, y= predict(lin_reg, newdata = dataset)), color= "blue") + #grafica de la recta
  ggtitle("Prediccion Lineal del sueldo del empleado") +
  xlab("Nivel del empleado") +
  ylab("Sueldo en U$D")

#Visualizacion del modelo Polinomico
ggplot() +
  geom_point(aes(x= dataset$Level , y= dataset$Salary ), color = "red") + #grafica de puntos 
  geom_line(aes(x = dataset$Level, y= predict(lin_pol, newdata = dataset)), color= "blue") + #grafica de la recta
  ggtitle("Prediccion Polinomica del sueldo del empleado") +
  xlab("Nivel del empleado") +
  ylab("Sueldo en U$D")

#Prediccion de nuevos resultados con Regresion Lineal
y_pred = predict(lin_reg, newdata = data.frame(Level = 6.5))

# Prediccion³n de nuevos resultados con Regresion³n PolinÃ³mica
y_pred_poly = predict(poly_reg, newdata = data.frame(Level = 6.5,
                                                     Level2 = 6.5^2,
                                                     Level3 = 6.5^3,
                                                     Level4 = 6.5^4))
