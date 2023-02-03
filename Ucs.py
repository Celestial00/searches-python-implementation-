
from queue import PriorityQueue

graph = { 

  'a': [(2, 'b'), (4,'c')],
  'b': [(4, 'd'), (6, 'e')],
  'c': [(7, 'f'), (9, 'h')]

}

visited = []
Queue = PriorityQueue()


def Usc(graph, cur_node, goal_node):
    
    visited.append(cur_node)
    Queue.put(0, cur_node)

    while not Queue.empty():

        if cur_node == goal_node:
            Queue.queue.clear()
            

        else: 

            if cur_node in visited:
                continue

            print(cur_node, end=" ")
            visited.append(cur_node)


            for neigh in graph[cur_node]:
                Queue.put((neigh[0], neigh[1]))

    