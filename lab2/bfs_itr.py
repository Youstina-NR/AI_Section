
from queue import Queue
def bfs_iterative(graph, start):
    queue = Queue(30)
    queue.put(start)
    v_nodes = []
    
    while (not queue.empty()):
        vertex = queue.get()
        
        if vertex in v_nodes:
            continue
        v_nodes.append(vertex)
        if vertex in graph:
            for neighbor in graph[vertex]:
                queue.put(neighbor)

    return v_nodes


graph1 = {1: [2, 3], 2: [4, 5],
          3: [5], 4: [6], 5: [6],
          6: [7], 7: []}

print(bfs_iterative(graph1, 1))

graph2 = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F']}
        #  'D': [],
        #  'E': [],
        #  'F': []}

print(bfs_iterative(graph2, 'A'))

print("X" in graph2)