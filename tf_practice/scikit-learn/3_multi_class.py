from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MultiLabelBinarizer

X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
y = [0, 0, 1, 1, 2]

classif = OneVsRestClassifier(estimator=SVC(random_state=0, gamma='scale'))
print(classif.fit(X, y).predict(X))

# 将目标向量转换为二值化后的二维数组
y = LabelBinarizer().fit_transform(y)
print(classif.fit(X, y).predict(X))

# 二值化多个标签产生二维数组并用来训练
y = MultiLabelBinarizer().fit_transform(y)
print(classif.fit(X, y).predict(X))

