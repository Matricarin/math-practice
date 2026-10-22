import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# создание графа из списка ребер

edges = [(1, 2), (2, 3), (1, 4), (1, 5)]

graph1 = nx.Graph()
graph1.add_edges_from(edges)

# создание графа из матрицы смежности

adj_matrix = np.array([
    [0, 1, 1],
    [1, 0, 0],
    [0, 0, 0]
])
graph2 = nx.from_numpy_array(adj_matrix)

# создание графа из списка степеней вершин

degrees = [4, 2, 2, 2, 2]
graph3 = nx.random_degree_sequence_graph(degrees)

# визуализация

plt.figure(figsize=(15,5))

plt.subplot(131)
nx.draw(graph1, with_labels=True)
plt.title("Список вершин")

plt.subplot(132)
nx.draw(graph2, with_labels=True)
plt.title("Матрица смежности")

plt.subplot(133)
nx.draw(graph3, with_labels=True)
plt.title("Список степеней")

plt.tight_layout()
plt.show()