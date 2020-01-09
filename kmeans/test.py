"""
kmeans
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import os
from sklearn.cluster import KMeans

d = io.imread(os.path.join('data', 'taibei101.jpg'))
d = np.array(d, dtype=np.float64)
d.shape
plt.axis('off')
plt.imshow(d)


# 利用K Means进行压缩
def KMeansImage(d, n_colors):
    w, h, c = d.shape
    dd = np.reshape(d, (w * h, c))
    km = KMeans(n_clusters=n_colors)
    km.fit(dd)
    labels = km.predict(dd)
    centers = km.cluster_centers_
    new_img = d.copy()
    for i in range(w):
        for j in range(h):
            ij = i * h + j
            new_img[i][j] = centers[labels[ij]]
    return {'new_image': new_img, 'center_colors': centers}

# 利用NMF进行压缩
def NMFImage(d, n_components):
    w, h, c = d.shape
    new_img = d.copy()
    for i in range(c):
        nmf = NMF(n_components=n_components)
        P = nmf.fit_transform(d[:, :, i])
        Q = nmf.components_
        new_img[:, : ,i] = np.clip(P @ Q, 0, 1)
    return {'new_image': new_img}

# 查看K Means在不同聚类个数下的视觉效果
plt.figure(figsize=(12, 9))
plt.imshow(d); plt.axis('off')
plt.show()
for i in [2, 3, 5, 10, 20, 30]:
    print('Number of clusters:', i)
    out = KMeansImage(d, i)
    centers, new_image = out['center_colors'], out['new_image']
    plt.figure(figsize=(12, 1))
    plt.imshow([centers]); plt.axis('off')
    plt.show()
    plt.figure(figsize=(12, 9))
    plt.imshow(new_image); plt.axis('off')
    plt.show()

# 查看NMF在不同成分个数下的视觉效果 
plt.figure(figsize=(12, 9))
plt.imshow(d); plt.axis('off')
plt.show()
for i in [1, 2, 3, 5, 10, 20, 30, 50, 80, 150]:
    print('Number of components:', i)
    out = NMFImage(d, i)
    new_image = out['new_image']
    plt.figure(figsize=(12, 9))
    plt.imshow(new_image); plt.axis('off')
    plt.show()