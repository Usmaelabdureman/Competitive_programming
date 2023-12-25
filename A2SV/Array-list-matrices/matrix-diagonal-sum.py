class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans =0
        n=len(mat)
        i=0
        j=0
        while i<=n-1 and j<=n-1:
            ans+=mat[i][j]
            i+=1
            j+=1
        i=n-1
        j=0
        while i>=0 and j<=n-1:
            ans+=mat[i][j]
            i-=1
            j+=1
        return ans-mat[n//2][n//2] if n%2 else ans
    
        