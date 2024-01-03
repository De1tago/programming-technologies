def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    unvisited = graph.copy()
    while unvisited:
        current_node = min(unvisited, key=lambda node: dist[node])
        unvisited.pop(current_node)
        for neighbor, weight in graph[current_node].items():
            new_dist = dist[current_node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
    return dist
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}
start_node = 'A'
print("Алгоритм Дейкстры:")
distances = dijkstra(graph, start_node)
for node, distance in distances.items():
    print("Расстояние от {} до {}: {}".format(start_node, node, distance))
print()


def euler_path (graph):
    # Проверяем, есть ли эйлеров цикл
    odd_vertices = [v for v in graph if len(graph[v]) % 2 != 0]
    if len(odd_vertices) > 2:
        return None
    start_vertex = odd_vertices[0] if odd_vertices else next(iter(graph))
    # Находим эйлеров путь
    path = []
    stack = [start_vertex]
    while stack:
        v = stack[-1]
        if graph[v]:
            u = graph[v].pop()
            graph[u].remove(v)
            stack.append(u)
        else:
            path.append(stack.pop())
    return path[::-1]  # Обратный порядок вершин
graph = {'A': ['B', 'D'], 'B': ['A', 'C', 'E'], 'C': ['B', 'E'], 'D': ['A', 'E'], 'E': ['B', 'C', 'D']}
path = euler_path (graph)
if path is None:
    print("Эйлеров цикл невозможен")
else:
    print("Эйлеров путь:", " -> ".join(path))


def topological_sort(graph):
    visited = set()
    stack = []
    def dfs(v):
        visited.add(v)
        for u in graph[v]:
            if u not in visited:
                dfs(u)
        stack.append(v)
    for v in graph:
        if v not in visited:
            dfs(v)
    return stack[::-1]
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
sorted_vertices = topological_sort(graph)
print("Топологическая сортировка: \nОтсортированные вершины:", " -> ".join(sorted_vertices))

import heapq

def prim(graph, start):
    mst = []
    visited = set([start])
    edges = [(cost, start, to) for to, cost in graph[start].items()]
    heapq.heapify(edges)
    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))
    return mst
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 4, 'D': 1},
    'C': {'A': 3, 'B': 4, 'D': 5},
    'D': {'B': 1, 'C': 5}
}
mst = prim(graph, 'A')
print("Алгоритм Прима:" )
for frm, to, cost in mst:
    print(frm, '->', to, '=', cost)

def kruskal(graph):
    mst = []
    parent = {}
    rank = {}
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]
    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 == root2:
            return
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1
    for v in graph:
        parent[v] = v
        rank[v] = 0
    edges = [(cost, v1, v2) for v1 in graph for v2, cost in graph[v1].items()]
    edges.sort()
    for cost, v1, v2 in edges:
        if find(v1) != find(v2):
            union(v1, v2)
            mst.append((v1, v2, cost))
    return mst
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 4, 'D': 1},
    'C': {'A': 3, 'B': 4, 'D': 5},
    'D': {'B': 1, 'C': 5}
}
mst = kruskal(graph)
print("Алгоритм Крускаля:" )
for frm, to, cost in mst:
    print(frm, '->', to, '=', cost)
