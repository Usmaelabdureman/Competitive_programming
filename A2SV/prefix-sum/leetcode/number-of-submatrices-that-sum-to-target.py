class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m,n = len(matrix),len(matrix[0])
        for row in range(m):
            for col in range(1,n):
                matrix[row][col] += matrix[row][col-1]
        count = 0
        for j1 in range(n):
            for j2 in range(j1,n):
                d = {0:1}
                curr_sum = 0
                for row in range(m):
                    curr_sum += matrix[row][j2] - (matrix[row][j1-1] if j1 > 0   else 0)
                    count += d.get(curr_sum-target,0)
                    d[curr_sum] = d.get(curr_sum,0)+1
        return count

                    