class Solution:
    def minCut(self, s: str) -> int:
        
        n = len(s)
        
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                is_pal[i][j] = s[i] == s[j] and (j - i < 3 or is_pal[i + 1][j - 1])
                
        min_cut = [i for i in range(n)]
        for i in range(n):
            for j in range(0, i + 1):
                if is_pal[j][i]:
                    min_cut[i] = min(min_cut[i], min_cut[j - 1] + 1) if j > 0 else 0
                    
        return min_cut[-1]