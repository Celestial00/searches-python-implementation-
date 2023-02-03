graph = {

    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'd': [],
    'c': ['f', 'g'],
    'f': [],
}


visited = []

def dfs(graph , visited, node):

    if node not in visited:
        visited.append(node)

        for neigh in graph(node):
            dfs(graph, visited, neigh)

dfs(graph, visited, 'a')