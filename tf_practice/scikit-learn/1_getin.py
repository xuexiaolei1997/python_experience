from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()  # 数据

clf = svm.SVC(gamma=0.001, C=100.)  # 分类器
clf.fit(digits.data[:-1], digits.target[:-1])  # 拟合，训练模型
pred = clf.predict(digits.data[-1:])  # 使用模型预测

# 对比预测与实际区别
print(pred)
print(digits.target[-1:])
print('pause')
