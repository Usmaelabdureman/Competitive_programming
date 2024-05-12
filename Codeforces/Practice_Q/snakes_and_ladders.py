from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_pos(num):
            num -= 1
            row = n - 1 - num // n
            col = num % n if row % 2 != n % 2 else n - 1 - num % n
            return row, col
        visited = set()
        queue = [(1, 0)]
        while queue:
            num, steps = queue.pop(0)
            if num == n * n:
                return steps
            if num in visited:
                continue
            visited.add(num)
            for i in range(1, 7):
                if num + i <= n * n:
                    row, col = get_pos(num + i)
                    if board[row][col] != -1:
                        queue.append((board[row][col], steps + 1))
                    else:
                        queue.append((num + i, steps + 1))
        return -1
        
sol = Solution()
print(sol.snakesAndLadders([[-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1],
                            [-1,35,-1,-1,13,-1],
                            [-1,-1,-1,-1,-1,-1],
                            [-1,15,-1,-1,-1,-1]])) #4