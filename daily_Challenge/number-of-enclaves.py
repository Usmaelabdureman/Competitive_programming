from typing import List
from collections import deque

class Solution:
    def bfs(self, x: int, y: int, m: int, n: int, grid: List[List[int]], visit: List[List[bool]]) -> None:
        q = deque()
        q.append((x, y))
        visit[x][y] = True

        dirx = [0, 1, 0, -1]
        diry = [-1, 0, 1, 0]

        while q:
            x, y = q.popleft()

            for i in range(4):
                r = x + dirx[i]
                c = y + diry[i]
                if r < 0 or r >= m or c < 0 or c >= n:
                    continue
                elif grid[r][c] == 1 and not visit[r][c]:
                    q.append((r, c))
                    visit[r][c] = True

    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            # First column.
            if grid[i][0] == 1 and not visit[i][0]:
                self.bfs(i, 0, m, n, grid, visit)
            # Last column.
            if grid[i][n - 1] == 1 and not visit[i][n - 1]:
                self.bfs(i, n - 1, m, n, grid, visit)

        for i in range(n):
            # First row.
            if grid[0][i] == 1 and not visit[0][i]:
                self.bfs(0, i, m, n, grid, visit)
            # Last row.
            if grid[m - 1][i] == 1 and not visit[m - 1][i]:
                self.bfs(m - 1, i, m, n, grid, visit)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visit[i][j]:
                    count += 1
        return count
