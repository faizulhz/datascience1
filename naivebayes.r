#NaiveBayes classifier tutorial
#Author: Faiz ul haque Zeya
#Data scientist,Associate professor BUKC

#first install e1071 package and load it
install.packages("e1071")
library(e1071)

#load the mlbench for HouseVotes dataset
library(mlbench)

#load the house vote dataset
data(HouseVotes84)

HouseVotes84
#you can see that first value is class, republicans or democrats.

HouseVotes84[1]

#Build the model Naive Bayes  ``
#predict class colum based on all others . means all others
model <- naiveBayes(Class ~ ., data = HouseVotes84)

# predict using model first 10 rows using 2 to 10 colums
predict(model, HouseVotes84[1:10,2:10])

