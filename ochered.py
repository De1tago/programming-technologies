
def bfs(graph, start, colors):
    queue = [start]
    colors[start] = 0

    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if colors[neighbor] == -1:
                colors[neighbor] = 1 - colors[vertex]
                queue.append(neighbor)
            elif colors[neighbor] == colors[vertex]:
                return False

    return True

graph = {
    0: [1, 3],
    1: [0, 3],
    2: [1, 2],
    3: [0, 1],
    4: [3, 4]
}
colors = [-1] * len(graph)

result = bfs(graph, 0, colors)
print(result, colors)
