import matplotlib.pyplot as plt
import numpy as np

def read_adjacency_matrix(file_path):
    adjacency_matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = [int(x) for x in line.split()]
            adjacency_matrix.append(row)
    return adjacency_matrix

def plot_adjacency_matrix(adjacency_matrix):
    plt.imshow(adjacency_matrix, cmap='binary', interpolation='none')
    plt.title('Adjacency Matrix')
    plt.xlabel('Nodes')
    plt.ylabel('Nodes')
    plt.colorbar()
    plt.show()

file_path = "text1.txt"  
adjacency_matrix = read_adjacency_matrix(file_path)
plot_adjacency_matrix(adjacency_matrix)
