class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        
        rows = len(grid)
        cols = len(grid[0])
        max_gold = 0

        def inbound(r,c):
            return 0 <= r < rows and 0 <= c < cols

        directions = {(0,-1),(0,1),(-1,0),(1,0)}

        def dfs(row, col):
            if not inbound(row,col) or grid[row][col] == 0:
                return 0

            max_gold = 0

            original_val = grid[row][col]
            grid[row][col] = 0


            for dx,dy  in directions:
                max_gold = max(max_gold, dfs(dx + row, dy + col))

            grid[row][col] = original_val
            return max_gold + original_val

        for row in range(rows):
            for col in range(cols):
                max_gold = max(max_gold, dfs(row,col))
        return max_gold