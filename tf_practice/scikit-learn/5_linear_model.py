import numpy as np
from sklearn import datasets
from sklearn import linear_model

# 糖尿病数据
diabetes = datasets.load_diabetes()
diabetes_X_train = diabetes.data[:-20]
diabetes_X_test = diabetes.data[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
print(regr.coef_)

# mse 均方误差
print(np.mean((regr.predict(diabetes_X_test) - diabetes_y_test)**2))

print(regr.score(diabetes_X_test, diabetes_y_test))
