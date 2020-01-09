from sklearn import svm
import numpy as np

# 生成数据
rng = np.random.RandomState(0)
X = rng.rand(100, 10)
y = rng.binomial(1, 0.5, 100)  # 二项分布
X_test = rng.rand(5, 10)
# 初始化分类器
clf = svm.SVC(gamma='scale')

# 设置分类器参数并训练
clf.set_params(kernel='linear').fit(X, y)
print(clf.predict(X_test))  # 输出预测结果

# 设置分类器参数并训练
clf.set_params(kernel='rbf').fit(X, y)
print(clf.predict(X_test))  # 输出预测结果
