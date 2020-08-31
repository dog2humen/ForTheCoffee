# coding:utf8

graph = {
    'A' : set(['B', 'C', 'F']),
    'B' : set(['A', 'D', 'E']),
    'C' : set(['A', 'F']),
    'D' : set(['B']),
    'E' : set(['B', 'F']),
    'F' : set(['A', 'C', 'E'])
}


def dfs_iter(graph, start):
    print(graph)
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for nextNode in graph[node]:
                if nextNode not in visited:
                    stack.append(nextNode)
    return visited


print(dfs_iter(graph, 'A'))


def dfs_recursive(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nextNode in graph[start]:
        if nextNode not in visited:
            dfs_recursive(graph, nextNode, visited)
    return visited

print(dfs_recursive(graph, 'A'))

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for nextNode in graph[node]:
                if nextNode not in visited:
                    queue.append(nextNode)
    return visited
