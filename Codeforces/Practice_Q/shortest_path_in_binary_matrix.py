from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] == 1:
            return -1
        
        directions = { (-1,-1),(-1,1),(-1,0),(0,-1),(0,1),(1,-1),(1,0),(1,1)}
        
        def inbound(r,c):
            return (0 <= r < n and 0 <= c < n)
        
        queue = deque()
        queue.append((0,0))
        grid[0][0] = 1
        
        ans = 1
        
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                if r == c == n - 1:
                    return ans
                for dx,dy in directions:
                    new_row , new_col = r + dx ,c + dy
                
                    if inbound(new_row,new_col) and grid[new_row][new_col] == 0:
                        grid[new_row][new_col] = 1
                        queue.append([new_row,new_col])
            ans += 1
        return -1
sol = Solution()
print(sol.shortestPathBinaryMatrix([[0,1],[1,0]])) #2
print(sol.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])) #4