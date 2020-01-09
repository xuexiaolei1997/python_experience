from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
import os
import numpy as np

iris_data_directory = 'iris_data'
model_name = os.path.join('iris_knn_model', 'iris_knn.model')

iris = datasets.load_iris()

# Feature: Flower length、Flower width、Petal length、Petal width
iris_X = iris.data

# Target classes: setosa,versicolor, virginica
iris_y = iris.target

# write data at directory: "iris_data"
with open(os.path.join(iris_data_directory, 'iris.csv'), 'w') as fout:
    a = np.array(iris_X, dtype=np.str)
    b = np.array(iris_y, dtype=np.str)
    for i in range(a.shape[0]):
        fout.write('%s,%s\n' % (','.join(a[i]), b[i]))

# Split and shuffle data
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)

# prepare model
knn = KNeighborsClassifier()

# train model
knn.fit(X_train, y_train)
# save model
joblib.dump(knn, model_name)

# print result predicted
print(knn.predict(X_test))
# print real result
print(y_test)
