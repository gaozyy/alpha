## classified the stocks to purchase

from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1],[2],[44],[77],[99],[88]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print(kmeans.labels_)