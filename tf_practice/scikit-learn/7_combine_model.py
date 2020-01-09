import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, decomposition, datasets
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

# 线性模型
logistic = linear_model.LogisticRegression()
# principle component analysis
pca = decomposition.PCA()
# pipe 管道，联合多种模型
pipe = Pipeline(steps=[('pca', pca), ('logistic', logistic)])

# 数据
digits = datasets.load_digits()
X_digits = digits.data
y_digits = digits.target

# pca拟合训练
pca.fit(X_digits)
# 画图
plt.figure(1, figsize=(4, 3))
plt.clf()
plt.axes([.2, .2, .7, .7])
plt.plot(pca.explained_variance_, linewidth=2)
plt.axis('tight')
plt.xlabel('n_components')
plt.ylabel('explained_variance_')

# GridSearchCV自动调参
n_components = [20, 40, 64]
Cs = np.logspace(-4, 4, 3)
estimator = GridSearchCV(pipe, dict(pca__n_components=n_components, logistic__C=Cs))
estimator.fit(X_digits, y_digits)

# 在轴上添加垂直线
plt.axvline(estimator.best_estimator_.named_steps['pca'].n_components, linestyle=':', label='n_components chosen')
plt.legend(prop=dict(size=12))
plt.show()
