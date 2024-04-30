
import random
import math
import pprint

# data cleaning function
def clean_data (points):
    points = []
    for i in lines:
        i=i.replace("?","")
        i=i.replace(","," ")
        points.append(i)

    final_points = []
    split_points = []
    for j in points:
        for x in j.split():
            split_points.append(float(x))
        final_points.append(split_points)
        split_points = []

    for ii in final_points[:]:
        if len(ii) < 3:
            final_points.remove(ii)

    for iii in final_points:
        if final_points.count(iii) > 1:
            final_points.remove(iii)

    return final_points


# distance calculate function
def calculate_distance (p, c):
    po = p
    ce = c
    d = math.sqrt((po[0] -  ce[0]) ** 2 + (po[1] -  ce[1]) ** 2 + (po[2] -  ce[2]) ** 2)
    return d

# K-means alghorithm function
def K_means (set_points, centroid):
    clusters = [
        {
            "center": center,
            "points": [],
        }
        for center in centroid
    ]

    dis = []
    for i in set_points:
        for j in centroid:
            di = calculate_distance (i,j)
            dis.append(di)
        ind = dis.index(min(dis))
        clusters[ind]["points"].append(i)
        dis = []

    return clusters

#############################################################

centroid = []
# reading file
with open("points.txt", "rt") as file:
    lines = file.readlines()

# points
set_points = clean_data(lines)

# centroid number
k = int(input("tedade khushe ar vared konid: "))

# generate random centroid
centroid = random.sample(set_points, k)

while True:
    f_clusters = K_means(set_points, centroid)
    new_centroid = []
    for cl in f_clusters:
        x, y, z = zip(*cl["points"])

        new_centroid.append(
            [
                sum(x) / len(x),
                sum(y) / len(y),
                sum(z) / len(z),
            ]
        )

    if centroid == new_centroid:
        break
    centroid = new_centroid


pprint.pprint(f_clusters)
