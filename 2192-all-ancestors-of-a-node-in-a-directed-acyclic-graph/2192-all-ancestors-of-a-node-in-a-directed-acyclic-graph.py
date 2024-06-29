class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(list)
        for u,v in edges:
            graph[v].append(u)
        

        ansest = [[] for _ in range(n)]

        i = 0

        while i < n:
            queue = deque([i])
            visited = set()
            while queue:
                node = queue.popleft()
                for par in graph[node]:
                    if par not in visited:
                        ansest[i].append(par)
                        queue.append(par)
                        visited.add(par)
            i += 1

        for i in range(n):
            ansest[i].sort()
        
        return ansest