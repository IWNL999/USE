from math import dist

DISTANCE = 1

def centroid(cluster):
    res = []
    for p1 in cluster:
        res.append((sum(dist(p1, p) for p in cluster), p1))
    return min(res)[1]

def get_neighbors(cluster_target):
    global data 
    for point in cluster_target:
        neighbors = [p for p in data if dist(p, point)<DISTANCE]
        cluster_target.extend(neighbors)
        data-=set(neighbors)

clusters = []
data = set([(float(n.split()[0]), float(n.split()[1])) for n in open('27/1_27a.txt')])
while data:
    clusters.append([data.pop()])
    for c in clusters:
        get_neighbors(c)
clusters = [c for c in clusters if len(c)>30]
centroids = [centroid(c) for c in clusters]
centroid_x = sum(centroid[0] for centroid in centroids)/len(centroids)
centroid_y = sum(centroid[1] for centroid in centroids)/len(centroids)
print(centroid_x*100000)
print(centroid_y*100000)