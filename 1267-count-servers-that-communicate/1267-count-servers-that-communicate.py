class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        row = [0] * m
        col = [0] * n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row[i] += 1
                    col[j] += 1
                    
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (row[i] > 1 or col[j] > 1):
                    ans += grid[i][j]
        return ans

    