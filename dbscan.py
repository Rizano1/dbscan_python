import numpy as np
import matplotlib.pyplot as plt
import random 

def n_centered_random(num_center, num_samples, std_dev=4):
    mean_x = random.sample(range(1, 100), num_center)
    mean_y = random.sample(range(1, 100), num_center)
    samples = []
    for i in range(num_center):
      j = 0
      while j < num_samples/3:
          x = random.normalvariate(mean_x[i], std_dev)
          y = random.normalvariate(mean_y[i], std_dev)
          sample = (x, y)
          if sample not in samples:
              samples.append(sample)
              j += 1
    return samples

def get_neighbors(data, point, eps):
    neighbors = []
    for i in range(len(data)):
        if np.linalg.norm(np.array(data[i]) - np.array(point)) < eps:
            neighbors.append(data[i])
    return neighbors

def dbscan(data, eps, min_pts):
    visited = []
    outliers = []
    cluster = []

    core_points = []
    non_core_points = []

    for i in range(len(data)):
        if len(get_neighbors(data, data[i], eps)) >= min_pts:
            core_points.append(data[i])
        else:
            non_core_points.append(data[i])

    def clustering(data, point, eps):
      neighbors = get_neighbors(data, point, eps)
      for neighbor in neighbors:
        if neighbor not in temp_cluster:
            temp_cluster.append(neighbor)
            core_points.remove(neighbor)
            clustering(data, neighbor, eps)
        else:
            continue
    
    while len(core_points) > 0:
        temp_cluster = []
        point = random.choice(core_points)
        clustering(core_points, point, eps)
        for no_core_point in non_core_points:
            if len(get_neighbors(temp_cluster, no_core_point, eps)) > 0:
                temp_cluster.append(no_core_point)
                non_core_points.remove(no_core_point)
        cluster.append(temp_cluster)

    for non_core_point in non_core_points:
        outliers.append(non_core_point)

    return cluster, outliers
        



if __name__ == "__main__":
    data = n_centered_random(3, 100)
    eps = 4
    min_pts = 4
    cluster, outliers = dbscan(data, eps, min_pts)
    print(cluster)

    my_colors = {1:'red',2:'green',3:'blue',4:'yellow',5:'purple',6:'orange',7:'pink',8:'brown',9:'cyan',10:'magenta'}


    # x,y = zip(*data)
    # plt.scatter(x, y)
    for i in range(len(cluster)):
        x, y = zip(*cluster[i])
        plt.scatter(x, y, color=my_colors[i+1])

    x, y = zip(*outliers)
    plt.scatter(x, y, color='black')

    plt.show()