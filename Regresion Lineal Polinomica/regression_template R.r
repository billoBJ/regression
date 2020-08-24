# Plantilla de Regresion

# Importar el dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[, 2:3]

# Dividir los datos en conjunto de entrenamiento y conjunto de test
# install.packages("caTools")
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$Purchased, SplitRatio = 0.8)
# training_set = subset(dataset, split == TRUE)
# testing_set = subset(dataset, split == FALSE)


# Escalado de valores
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])

# Ajustar Modelo de RegresiÃ³n con el Conjunto de Datos
# Crear nuestra variable de Regresion aquÃ�



# Prediccion de nuevos resultados con Regresion 
y_pred = predict(regression, newdata = data.frame(Level = 6.5))



# Visualizacion del modelo de Regresion
# install.packages("ggplot2")
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() +
  geom_point(aes(x = dataset$Level , y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = x_grid, y = predict(regression, 
                                        newdata = data.frame(Level = x_grid))),
            color = "blue") +
  ggtitle("PredicciÃ³n (Modelo de RegresiÃ³n)") +
  xlab("Nivel del empleado") +
  ylab("Sueldo (en $)")