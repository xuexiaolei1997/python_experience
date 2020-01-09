from sklearn.externals import joblib
import numpy as np
import os
import re

# read model
model_name = os.path.join('iris_knn_model', 'iris_knn.model')
knn = joblib.load(model_name)

# input data and output result
my_data = input("Please Enter the four features(split by ' ' or ','):")
my_data = np.array(re.split('\s+|,', my_data), dtype=np.float).reshape((1, -1))
print(knn.predict(my_data))
