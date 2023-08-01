class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        result = []
        
        def dfs(node, path):
            if node == n - 1:
                result.append(path)
                return
            
            for neighbor in graph[node]:
                dfs(neighbor, path + [neighbor])
        
        dfs(0, [0])
        return result
