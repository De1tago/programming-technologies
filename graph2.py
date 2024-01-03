import networkx as nx
import matplotlib.pyplot as plt
#3.Дан ориентированный граф. Вывести все вершины, достижимые из данной.

target_vertex = int(input())
def find_reachable_vertices(graph, target):
    reachable_vertices = set()  # Множество достижимых вершин
    stack = [target]  # Стек для обхода в глубину

    while stack:
        vertex = stack.pop()
        reachable_vertices.add(vertex)

        # Проверяем все соседние вершины, если они еще не были посещены
        for neighbor in graph.neighbors(vertex):
            if neighbor not in reachable_vertices:
                stack.append(neighbor)

    return reachable_vertices

# Создание ориентированного графа
graph = nx.DiGraph()
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
# graph.add_edge(3, 1)
# graph.add_edge(5, 1)
#-------------
graph.add_edge(6, 7)
graph.add_edge(7, 6)


# target_vertex = 3
pos = nx.spring_layout(graph)
reachable_vertices = find_reachable_vertices(graph, target_vertex)
print("Вершины, из которых существует путь в вершину", target_vertex, ":", reachable_vertices)

nx.draw(graph, pos, with_labels=True) 
plt.show()