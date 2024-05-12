class Solution:
    def largestLocal(self, grid):
        def find_max(x, y):
            max_elt = 0
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    max_elt = max(max_elt, grid[i][j])

            return max_elt
        N = len(grid)
        
        max_local = [[0] * (N - 2) for _ in range(N - 2)]
        for i in range(N - 2):
            for j in range(N - 2):
                max_local[i][j] = find_max( i, j)
        
        return max_local