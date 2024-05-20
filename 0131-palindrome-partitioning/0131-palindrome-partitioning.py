class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            
            for j in range(i, n):

                dp[i][j] = s[i] == s[j] and (abs(i - j) <= 1 or dp[i + 1][j - 1])

        def dfs(s, i, t):
            nonlocal n
            if i == n:
                ans.append(t[:])
                return
            for j in range(i, n):
                if dp[i][j]:
                    t.append(s[i : j + 1])
                    dfs(s, j + 1, t)
                    t.pop(-1)

        dfs(s, 0, [])
        return ans