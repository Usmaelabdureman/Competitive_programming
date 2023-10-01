class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            grid[row][col] = '0'  # Mark the cell as visited

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        queue.append((nr, nc))
                        grid[nr][nc] = '0'  # Mark the cell as visited

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    num_islands += 1
                    bfs(row, col)  # Explore the island and mark its cells as visited

        return num_islands
