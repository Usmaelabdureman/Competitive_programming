class Solution:
    
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        # Check for empty matrices
        if not matrix or not matrix[0]:
            return []
        n=len(matrix)
        m=len(matrix[0])
        res=[]

        def recur(r,c):

            if r == n-1 and c == m-1:
                res.append(matrix[r][c])
                return res
            visited.add((r,c))

            res.append(matrix[r][c])
            if (r+c)%2 == 0 :
                if r-1 >=0 and c +1 <=m-1:
                    if (r-1,c+1) not in visited:
                        recur(r-1,c+1)
                elif c+1 < m:
                    if (r,c+1) not in visited:
                        recur(r,c+1)
                elif r+1 < n:
                    if (r+1,c) not in visited:
                        recur(r+1,c)
            else:
                if r+1 <=n-1 and c -1>=0:
                    if (r+1,c-1) not in visited:
                        recur(r+1,c-1)
                elif r+1 < n:
                    if (r+1,c) not in visited:
                        recur(r+1,c)
                elif c+1 < m:
                    if (r,c+1) not in visited:
                        recur(r,c+1)

        recur(0,0)
        return res