class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        ones_row = [0] * m
        ones_col = [0] * n
        
        for i in range(m):
            for j in range(n):
                ones_row[i] += grid[i][j]
                ones_col[j] += grid[i][j]
        
        diff = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = 2 * ones_row[i] + 2 * ones_col[j] - n - m
        
        return diff
