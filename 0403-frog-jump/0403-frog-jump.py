class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        mark = {}
        dp = [[False] * 2001 for _ in range(n)]

        # Mark stones in the dictionary to identify if such stone exists or not.
        for i in range(n):
            mark[stones[i]] = i

        dp[0][0] = True
        for index in range(n):
            for prevJump in range(n + 1):
                # If stone exists, mark the value with position and jump as 1.
                if dp[index][prevJump]:
                    if stones[index] + prevJump in mark:
                        dp[mark[stones[index] + prevJump]][prevJump] = True
                    if stones[index] + prevJump + 1 in mark:
                        dp[mark[stones[index] + prevJump + 1]][prevJump + 1] = True
                    if prevJump - 1 > 0 and stones[index] + prevJump - 1 in mark:
                        dp[mark[stones[index] + prevJump - 1]][prevJump - 1] = True

        # If any value with index as n - 1 is true, return true.
        for index in range(n):
            if dp[n - 1][index]:
                return True
        return False
