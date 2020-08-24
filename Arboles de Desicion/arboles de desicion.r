# Arbol de Decision para Regresion

# Importar el dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[, 2:3]

# Ajustar Modelo de Regresion con el Conjunto de Datos
#install.packages("rpart")
library(rpart)
regression = rpart(formula = Salary ~ .,
                   data = dataset,
                   control = rpart.control(minsplit = 1))

# PredicciÃ³n de nuevos resultados con Arbol Regresion
y_pred = predict(regression, newdata = data.frame(Level = 6.5))



# VisualizaciÃ³n del modelo de Arbol de Regresion
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() +
  geom_point(aes(x = dataset$Level , y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = x_grid, y = predict(regression, 
                                        newdata = data.frame(Level = x_grid))),
            color = "blue") +
  ggtitle("PredicciÃ³n con Ãrbol de DecisiÃ³n (Modelo de RegresiÃ³n)") +
  xlab("Nivel del empleado") +
  ylab("Sueldo (en $)")
