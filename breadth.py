
graph = {

    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'd': [],
    'c': ['f', 'g'],
    'f': [],
}


visited = []
queue = []

def bfs(graph, visited, node):

    visited.append(node)
    queue.append(node)



    while queue is not None:
        
        m = queue.pop(0)

        for n in graph[m]:
            if n not in visited:
                visited.append(n)
                queue.append(n)