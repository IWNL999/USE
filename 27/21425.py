from math import *

DISTANCE = 2

def centroid(cluster):
    res = []
    for p in cluster:
        res.append((sum(dist(p, p1) for p1 in cluster), p))
    return min(res)[1]

def get_neighbors(cluster_target):
    global data
    for point in cluster_target:
        neighbors = [p for p in data if dist(point, p) < DISTANCE]
        cluster_target.extend(neighbors)
        data -= set(neighbors)

clusters = []
data = set([(float(n.split()[0]), float(n.split()[1])) for n in open('27/27_A_21425.txt')])

while data:
    clusters.append([data.pop()])
    for c in clusters:
        get_neighbors(c)

centroids = [centroid(c) for c in clusters]

centroid_x = sum([centroid[0] for centroid in centroids])/len(centroids)
centroid_y = sum([centroid[1] for centroid in centroids])/len(centroids)
print(centroid_x*10000)
print(centroid_y*10000)