class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # If the starting cell or ending cell has an obstacle, there's no path
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1  # There's only one way to reach the starting cell
        
        # Fill the first column
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] == 0 else 0
        
        # Fill the first row
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] if obstacleGrid[0][j] == 0 else 0
        
        # Fill the rest of the cells
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
