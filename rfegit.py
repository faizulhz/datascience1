#Faiz ul haque Zeya
#Recursive feature elimination with SVM with various no. of features
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n
from sklearn.svm import LinearSVC
from sklearn.feature_selection import RFE
from sklearn import datasets
dataset = datasets.load_iris()
#select Linear SVC with recursive feature extraction with 4 frearues
svm = LinearSVC()
rfe = RFE(svm, 4)
rfe = rfe.fit(dataset.data, dataset.target)
#predict the data set
a=rfe.predict(dataset.data[:])
#print the predcited
#print the target
b=dataset.target[:]
#Calculate error
error=np.array(a-b)
notzero = (error != 0).sum()
print("Number of misclassified 4 feaures::",notzero)  
rfe = RFE(svm, 3)
rfe = rfe.fit(dataset.data, dataset.target)
#predict the data set
a=rfe.predict(dataset.data[:])
#print the predcited
#print the target
b=dataset.target[:]
#Calculate error
error=np.array(a-b)
notzero = (error != 0).sum()
print("Number of misclassified WITH 3 feaures:",notzero)  
rfe = RFE(svm, 6)
rfe = rfe.fit(dataset.data, dataset.target)
#predict the data set
a=rfe.predict(dataset.data[:])
#print the predcited

#print the target
b=dataset.target[:]

#Calculate error
error=np.array(a-b)
notzero = (error != 0).sum()
print("Number of misclassified with 6 features:",notzero)  
rfe = RFE(svm, 7)
rfe = rfe.fit(dataset.data, dataset.target)
#predict the data set
a=rfe.predict(dataset.data[:])
#print the predcited

#print the target
b=dataset.target[:]

#Calculate error
error=np.array(a-b)
notzero = (error != 0).sum()
print("Number of misclassifiedwith 7 feaures:",notzero)  
