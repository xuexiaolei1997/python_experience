from time import time
import logging
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import fetch_lfw_people
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
from sklearn.svm import SVC
logging.basicConfig(level=logging.INFO, format='%(asctime)s % (message)s')

# 筛选 - 指定文件夹，不下载，最少图片数量
lfw_people = fetch_lfw_people(data_home='lfw_funneled', funneled=False, min_faces_per_person=70, resize=0.4)

# 高（图片个数）， 长， 宽
n_samples, h, w = lfw_people.images.shape
X = lfw_people.data
n_features = X.shape[1]  # 图片像素：长 x 宽

y = lfw_people.target  # 向量
target_names = lfw_people.target_names
n_classes = target_names.shape[0]

print('Total dataset size:')
print('n_samples:%d' % n_samples)
print('n_features:%d' % n_features)
print('n_classes:%d' % n_classes)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# PCA
n_components = 150  # 特征数
print('Extracting the top %d eigenfaces from %d faces' % (n_components, X_train.shape[0]))
t0 = time()
pca = PCA(n_components=n_components, svd_solver='randomized', whiten=True).fit(X_train)
print('done in %0.3fs' % (time() - t0))

eigenfaces = pca.components_.reshape((n_components, h, w))
print('Projecting the input data on the eigenfaces orthonormal basis')
t0 = time()
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print('done in %0.3fs' % (time() - t0))

# SVM
print('Fitting the classifier to the training set')
t0 = time()
param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5], 'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1]}
clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)
clf = clf.fit(X_train_pca, y_train)
print('done in %0.3fs' % (time() - t0))
print('Best estimator found by grid search:')
print(clf.best_estimator_)

# 质量检测
print('Predicting people\'s names on the test set')
t0 = time()
y_pred = clf.predict(X_test_pca)
print('done in %0.3f' % (time() - t0))
print(classification_report(y_test, y_pred, target_names=target_names))
print(confusion_matrix(y_test, y_pred, labels=range(n_classes)))


def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    plt.figure(figsize=(1.8*n_col, 2.4*n_row))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.9, hspace=.35)
    for i in range(n_row*n_col):
        plt.subplot(n_row, n_col, i+1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())


def title(y_pred, y_test, target_names, i):
    pred_name = target_names[y_pred[i]].rsplit(' ', 1)[-1]
    true_name = target_names[y_test[i]].rsplit(' ', 1)[-1]
    return 'predicted: %s\ntrue: %s' % (pred_name, true_name)


prediction_titles = [title(y_pred, y_test, target_names, i) for i in range(y_pred.shape[0])]
plot_gallery(X_test, prediction_titles, h, w)
plt.show()
