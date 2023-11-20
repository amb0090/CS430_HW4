import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def main():

    # Read the Iris dataset from "iris.data" file
    column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
    iris_data = pd.read_csv('iris.data', header=None, names=column_names)

    # Separate feature data and class labels
    X = iris_data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
    Y = iris_data[['class']].values

    # Initialize K-means with the number of clusters you want to create
    kmeans = KMeans(n_clusters=3, init='random', random_state=42)

    # Fit the K-means model to the data
    kmeans.fit(X)

    # Get cluster labels for each data point
    labels = kmeans.labels_

    # Get and report the cluster centers
    cluster_centers = kmeans.cluster_centers_
    with open('output.txt', 'w') as w:
        for i in range(3):
            w.write(f'Cluster {i+1} centroid: {cluster_centers[i,:]}')
            w.write('\n')
    
    # Visualize the clusters
    plt.figure(figsize=(10, 6))

    # Scatter plot for each cluster
    for i in range(3):
        plt.scatter(X[labels == i, 0], X[labels == i, 1], label=f'Cluster {i + 1}')

    # Plot the cluster centers as well
    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s=200, c='red', label='Cluster Centers', marker='X')

    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.title('K-means Clustering of Iris Dataset')
    plt.legend()
    plt.show()

    # This code writes the iris data to a file in the format
    # used with LibSVM
    with open('iris_libsvm.txt', 'w') as f:
        for i in range(len(X)):
            class_label = 0
            if Y[i] == 'Iris-setosa':
                class_label = 0
            elif Y[i] == 'Iris-versicolor':
                class_label = 1
            else:
                class_label = 2

            # Write the class label
            f.write(f'{class_label} ')

            # Write the feature-value pairs
            for j in range(len(X[i])):
                f.write(f'{j + 1}:{X[i][j]} ')

            # Write a newline character to separate data points
            f.write('\n')


if __name__ == '__main__':
    main()
