class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxValInRows = [max(row) for row in grid]
        maxValInCols = [max(col) for col in zip(*grid)]
        
        return sum(min(maxValInRows[r], maxValInCols[c]) - val for r, row in enumerate(grid) for c, val in enumerate(row))