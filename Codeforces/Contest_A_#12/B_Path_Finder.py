from collections import defaultdict


n = int(input())

grid = []

for i in range(n-1):
    nodes = list(map(int, input().split()))
    grid.append(nodes)
    
# print(grid)

graph = defaultdict(list)

for u, v, c in grid:
    graph[u].append((v, c))
    graph[v].append((u, c))
    
# print(graph)

max_dist = 0

def dfs(node = 0, par = -1, curr_dist = 0):
    global max_dist
    max_dist = max(max_dist, curr_dist)
    for neigh, wei in graph[node]:
        if neigh != par:
            dfs(neigh, node, curr_dist + wei)
dfs()
print(max_dist)