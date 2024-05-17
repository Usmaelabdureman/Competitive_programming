class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        n = len(t)
        dp = [1] + [0] * n
        for a in s:
            for j in range(n, 0, -1):
                if a == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[n]