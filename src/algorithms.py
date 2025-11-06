import numpy as np

class KMeans:
    def __init__(self, n_clusters=8, max_iter=300, tol=1e-4):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol
        self.centroids = None

    def fit(self, X):
        random_indices = np.random.choice(len(X), self.n_clusters, replace=False)
        self.centroids = X[random_indices]

        for _ in range(self.max_iter):
            distances = self._compute_distances(X)
            labels = np.argmin(distances, axis=1)

            new_centroids = []
            for i in range(self.n_clusters):
                cluster_points = X[labels == i]
                if len(cluster_points) > 0:
                    new_centroids.append(cluster_points.mean(axis=0))
                else:
                    new_centroids.append(self.centroids[i])
            new_centroids = np.array(new_centroids)

            if np.all(np.abs(new_centroids - self.centroids) < self.tol):
                break

            self.centroids = new_centroids

    def predict(self, X):
        distances = self._compute_distances(X)
        return np.argmin(distances, axis=1)

    def _compute_distances(self, X):
        return np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)


class DBSCAN:
    def __init__(self, eps=0.5, min_samples=5):
        self.eps = eps
        self.min_samples = min_samples
        self.labels = None

    def fit(self, X):
        n_samples = X.shape[0]
        self.labels = -np.ones(n_samples)
        cluster_id = 0

        for i in range(n_samples):
            if self.labels[i] != -1:
                continue

            neighbors = self._get_neighbors(X, i)
            if len(neighbors) < self.min_samples:
                self.labels[i] = -1
                continue

            self.labels[i] = cluster_id
            self._expand_cluster(X, neighbors, cluster_id)
            cluster_id += 1

    def _expand_cluster(self, X, neighbors, cluster_id):
        for neighbor in neighbors:
            if self.labels[neighbor] == -1:
                self.labels[neighbor] = cluster_id

            if self.labels[neighbor] != -1:
                continue

            self.labels[neighbor] = cluster_id
            new_neighbors = self._get_neighbors(X, neighbor)
            if len(new_neighbors) >= self.min_samples:
                neighbors = np.concatenate((neighbors, new_neighbors))

    def _get_neighbors(self, X, index):
        distances = np.linalg.norm(X - X[index], axis=1)
        return np.where(distances < self.eps)[0]