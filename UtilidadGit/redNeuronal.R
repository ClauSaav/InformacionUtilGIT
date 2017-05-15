train<-iris[sample(1:150,30),]
train

train$setosa <-c(train$Species=="setosa")
train$versicolor <-c(train$Species=="versicolor")
train$virginica <-c(train$Species=="virginica")
train

library(neuralnet)
net.inet<-neuralnet(setosa + versicolor + virginica ~ Sepal.Length + Sepal.Width + Petal.Length + Petal.Width, train, hidden=3, lifesign = "full", algorithm = "rprop+")

plot(net.inet, rep = "best")
plot(net.inet, rep = "best", intercept = FALSE)

predict<-compute(net.inet, iris[1:4])
predict
which.max(predict$net.result[1:4])
result<-0

for(i in 1:150) { result[i] <- which.max(predict$net.result[i,])}
for(i in 1:150) { if (result[i] ==1) { result[i]="setosa"}}
for(i in 1:150) { if (result[i] ==2) { result[i]="versicolor"}}
for(i in 1:150) { if (result[i] ==3) { result[i]="virginica"}}

comparison <- iris
comparison$Predicted <- result
comparison

(MC <- table(iris$Species,result))


