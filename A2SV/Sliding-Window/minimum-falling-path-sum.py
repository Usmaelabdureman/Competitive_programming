class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for r in range(1, len(matrix)):
            for c in range(len(matrix[0])):
                if c == 0:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c+1])
                elif c == len(matrix[0])-1:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c-1])
                else:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c+1], matrix[r-1][c-1])
        return min(matrix[-1])