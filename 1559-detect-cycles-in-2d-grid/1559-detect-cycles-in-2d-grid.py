class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = set()
        
        def dfs(row, col, prev_row, prev_col, target):
            if (row, col) in visited:
                return True
            
            visited.add((row, col))
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and (new_row, new_col) != (prev_row, prev_col) and grid[new_row][new_col] == target:
                    if dfs(new_row, new_col, row, col, target):
                        return True
                    
            return False
        
        for row in range(m):
            for col in range(n):
                if (row, col) not in visited:
                    if dfs(row, col, -1, -1, grid[row][col]):
                        return True
        
        return False
