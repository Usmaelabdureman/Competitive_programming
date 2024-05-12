from heapq import heapify,heappop,heappush
from collections import defaultdict

def UCS(graph, start, goal):
    
    queue = [(0, start)]
    heapify(queue)
    visited = set()
    path = []
    while queue:
        cost , node = heappop(queue)
        # 
        if node in visited:
            continue
        # 
        visited.add(node)
        path.append(node)
        # 
        if node == goal:
            return path, cost
        # 
        for neigh, c in graph[node]:
            if neigh not in visited:
                heappush(queue,(cost + c,neigh)) 
    return path, cost

data =[
    ('A', 'B', 5),
    ('A', 'D', 3),
    ('B', 'C', 1),
    ('C', 'G', 8),
    ('C', 'E', 6),
    ('D', 'E', 2),
    ('D', 'F', 2),
    ('E', 'B', 4),
    ('G', 'E', 4),
    ('F', 'G', 3)
]

graph = defaultdict(list)
for u, v, w in data:
    graph[u].append((v, w))
    graph[v].append((u, w))
    
traversed_path, actual_path = UCS(graph, 'A', 'G')
print(traversed_path)
print(actual_path)