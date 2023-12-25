class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans =0
        n=len(mat)
        for i in range(n):
            for j in range(n):
                if i ==j:
                    ans+=mat[i][j]

        i=n-1
        j=0
        while i>=0 and j<=n-1:
            ans+=mat[i][j]
            i-=1
            j+=1
        return ans-mat[n//2][n//2] if n%2 else ans
    
        