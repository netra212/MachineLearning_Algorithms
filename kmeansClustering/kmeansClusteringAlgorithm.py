from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt 
import random 
import numpy as np

centroids = [(-5,-5),(5,5)]
cluster_std = [1,1]

X,y = make_blobs(n_samples=100, cluster_std=cluster_std, centers=centroids, n_features=2, random_state=2)

"""
steps to perform the clustering algorithms:
1. Decide #clusters. 
2. select random centroids. 
3. Assign clusters. 
4. Move centroids. 
5. check finish.
"""
class KMeans:

    def __init__(self, nClusters=2, max_iter=100):
        self.nClusters = nClusters
        self.max_iter = max_iter 
        self.centroids = None 
    
    def fit_predict(self):
        # range of sampling. 
        random_index = random.sample(range(0, X.shape[0]), self.nClusters)

        # 
        for i in range(self.max_iter):
            # assign clusters.
            cluster_group = self.assign_clusters(X) #[1,0,0,1,1]
            old_centroids = self.centroids
            # move centroids.
            self.centroids = self.move_centroids(X, cluster_group) 
            # check finish.
            if (old_centroids == self.centroids).all:
                break

        return cluster_group

    def assign_clusters(self,X):
        cluster_group = []
        # each point ko each centroids sanga ko distance calculate garna parcha.
        distances = [] 
        for row in X:
            for centroid in self.centroids:
                # calculate the euclidean distance between current centroid and current row. 
                # formula = sqrt((x2-x1)^2 + (y2-y1)^2)
                # This is (x2-x1)(x2-x1) + (y2-y1)(y2-y1) the dot product of the (x2-x1)(y2-y1) and (x2-x1)(y2-y1) 
                # General formula of euclidean distance in any number of dimensions: => np.sqrt(np.dot(b-b, b-a))
                distances.append(np.sqrt(np.dot(row-centroids, row-centroids)))
            print(distances) # each row ko lagii 2 ta distances calculate huncha.
            # storing the min distances. 
            min_distance = min(distances)
            # index position of the min distances. 
            index_pos = distances.index(min_distance)

            cluster_group.append(index_pos)
            distances.clear()

        return np.array(cluster_group)

    def move_centroids(self, X, cluster_group):
        new_centroids = []

        cluster_type = np.unique(cluster_group)

        for type in cluster_type:
            new_centroids.append(X[cluster_group==type].mean(axis=0))

        return np.array(new_centroids)

km = KMeans(nClusters=2, max_iter=100)
km.fit_predict(X)




