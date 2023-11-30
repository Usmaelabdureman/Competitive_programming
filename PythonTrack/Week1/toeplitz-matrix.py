class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # print(len(matrix))
        # print(len(matrix[0]))
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
            