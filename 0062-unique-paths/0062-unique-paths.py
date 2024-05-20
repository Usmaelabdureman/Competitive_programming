class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def uniquePathsRec(coord):
            row , col = coord
            if coord == (m - 1,n - 1):
                return 1
            ways = 0
            if row + 1 < m:
                ways += uniquePathsRec((row + 1, col))
            if col + 1 < n:
                ways += uniquePathsRec((row, col + 1))
            return ways
        return uniquePathsRec((0,0))