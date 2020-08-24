# Importar el dataset
dataset = read.csv('50_Startups.csv')

# Codificar las variables categoricas
dataset$State = factor(dataset$State,
                       levels = c("New York", "California", "Florida"),
                       labels = c(1, 2, 3))

# Dividir los datos en conjunto de entrenamiento y conjunto de test
library(caTools)
set.seed(123)
#profit es la columna a predecir 
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)



# Ajustar el modelo de Regresion Lineal Multiple 
#con el Conjunto de Entrenamiento
regression = lm(formula = Profit ~ .,
                data = training_set)


# Predecir los resultados con el conjunto de testing
y_pred = predict(regression, newdata = testing_set)

# Construir un modelo optimo con la Eliminacion hacia atras

#valor minimo para el p-value
#los coeficientes que tengan un p-value mayor 
#seran eliminado de la formula del modelo de prediccion 
SL = 0.05  #nivel de significancia 

regression = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
                data = dataset)
summary(regression)

regression = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
                data = dataset)
summary(regression)

regression = lm(formula = Profit ~ R.D.Spend + Marketing.Spend,
                data = dataset)
summary(regression)

regression = lm(formula = Profit ~ R.D.Spend,
                data = dataset)
summary(regression)