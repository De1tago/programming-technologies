#10. Дан неориентированный граф. Удалить ребро, соединяющее вершины 𝑎 и 𝑏.


import networkx as nx
import matplotlib.pyplot as plt

def remove_edge(graph, a, b):
    graph.remove_edge(a, b)

# Создание графа
graph = nx.Graph()
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 5)
graph.add_edge(1, 3)

#edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (5, 5)]
# Визуализация исходного графа
pos = nx.spring_layout(graph)  # Определение позиций вершин для отображения
nx.draw(graph, pos, with_labels=True)  # Отрисовка графа
plt.title('Исходный граф')
plt.show()

# Удаление ребра и визуализация измененного графа
remove_edge(graph, 2, 3)

nx.draw(graph, pos, with_labels=True)  # Отрисовка графа после удаления ребра
plt.title('Граф после удаления ребра (2, 3)')
plt.show()