#Step 1 - Loading the Required Libraries and Modules
# Import required libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sklearn
from sklearn import metrics
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor

# Import necessary modules
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score

# Step 2 - Reading the Data and Performing Basic Data Checks
df = pd.read_csv('diabetes.csv') 
print(df.shape)
print(df.describe().transpose())

# Step 3 - Creating Arrays for the Features and the Response Variable
target_column = ['Outcome'] 
# features = list(set(list(df.columns))-set(target_column))
features = df.columns[:-1]
df[features] = df[features]/df[features].max()
print(df.describe().transpose())

# Step 4 - Creating the Training and Test Datasets
X = df[features]
y = df[target_column].values.ravel()
print(y.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=40)
print(X_train.shape)
print(X_test.shape)

from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(8,8,8), activation='relu', solver='adam', max_iter=600)
mlp.fit(X_train,y_train)

predict_train = mlp.predict(X_train)
predict_test = mlp.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_train,predict_train))
print(classification_report(y_train,predict_train))

print(confusion_matrix(y_test,predict_test))
print(classification_report(y_test,predict_test))
print(metrics.accuracy_score(y_test,predict_test))





