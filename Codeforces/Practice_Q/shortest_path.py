
""" The undirected graph is given. Find the shortest path from vertex a to vertex b.

Input
The first line contains two integers n and m (1 ≤ n ≤ 5 * 104, 1 ≤ m ≤ 105) - the number of vertices and edges. The second line contains two integers a and b - the starting and ending point correspondingly. Next m lines describe the edges.

Output
If the path between a and b does not exist, print -1. Otherwise print in the first line the length l of the shortest path between these two vertices in number of edges, and in the second line print l + 1 numbers - the vertices of this path.

"""

from typing import List
from collections import deque

class Solution:
    def shortest_path(self, n:int, m:int, a:int):
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        a, b = map(int, input().split())
        visited = [False] * (n + 1)
        visited[a] = True
        queue = deque([(a, 0)])
        while queue:
            v, d = queue.popleft()
            if v == b:
                return d
            for u in graph[v]:
                if not visited[u]:
                    visited[u] = True
                    queue.append((u, d + 1))
        return -1
    
sol = Solution()
n, m = map(int, input().split())
a = int(input())
print(sol.shortest_path(n, m, a))

    