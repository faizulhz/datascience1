#ggplot tutorial
#Faiz ul haque Zeya
#Data scientist and Associate professor
#CEO Transys
#version 1.0




#install and load the library ggplot2.
install.package("ggplot2")
library(ggplot2)


#quickplot qlot the diamond dataset and  mtcars
qplot(carat, price, data = diamonds)
qplot(wt,mpg,data=mtcars)

#now use ggplot for the same
q <- ggplot(diamonds,aes(carat,price))
q + geom_point()

q <- ggplot(mtcars,aes(wt,mpg))
q + geom_point()

#with smooting predicting
q <- ggplot(diamonds,aes(carat,price))
q + geom_point()+ geom_smooth()

q <- ggplot(mtcars,aes(wt,mpg))
q + geom_point()+ geom_smooth()



#color points in qplot
qplot(carat, price, data = diamonds,colour=color)
qplot(wt,mpg,data=mtcars,colour=color)

#color points in qplot with shape
qplot(carat, price, data = diamonds,colour=color,shape=cut)
qplot(wt,mpg,data=mtcars,colour=color,shape=cut)

#from opaque to tranparent
qplot(wt,mpg,data=mtcars,colour=color,alpha=I(1/10))


#geom is used to create various types of plots
#boxplot 
qplot(wt,mpg,data=mtcars,geom="boxplot")
#histogram
qplot(wt,data=mtcars,geom="histogram")
