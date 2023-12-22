class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # method one

        # Rotate Groups of Four Cells
        n = len(matrix[0])
        # for i in range(n//2+n%2):
        #     for j in range(n//2):
        #         temp = matrix[n-1-j][i]
        #         matrix[n-1-j][i]=matrix[n-1-i][n-j-1]
        #         matrix[n-1-i][n-j-1]=matrix[j][n-1-i]
        #         matrix[j][n-1-i]=matrix[i][j]
        #         matrix[i][j]=temp

        # method 2

        #  transpose + reverse = Rotate

        # transpose matrix
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        #  reverse matrix
        for i in range(n):
            matrix[i].reverse()