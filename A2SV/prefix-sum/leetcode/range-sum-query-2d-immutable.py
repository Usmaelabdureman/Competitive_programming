class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows , cols = len(matrix), len(matrix[0])
        self.submatrix_sum = [[0]*(cols+1) for r in range(rows+1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                self.submatrix_sum[r+1][c+1] = self.submatrix_sum[r][c+1] + prefix
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,row2,col1,col2 = row1+1,row2+1,col1+1,col2+1
        ans = self.submatrix_sum[row2][col2] - self.submatrix_sum[row2][col1 - 1] - self.submatrix_sum[row1 - 1][col2 ] + self.submatrix_sum[row1 - 1][col1 - 1]
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)