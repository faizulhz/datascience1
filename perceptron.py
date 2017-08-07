#Faiz ul haque Zeya
#SK learn Perceptron
import numpy as np
import pandas as pd
from sklearn import linear_model
df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None)
df.tail()
y=df.iloc[0:100,4].values
print(y)
y=np.where(y=='Iris-setosa',-1,1)
print(y)
X=df.iloc[0:100,0:4].values
p=linear_model.Perceptron(eta0=0.1,n_iter=10)
print(X)
p.fit(X,y)
b=[6.7,3.0,5.2,2.3]
a=p.predict(b)				
print("The output class for ",b," is ",a)
