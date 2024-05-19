class Solution:
    def stoneGame(self, piles):
        
        @cache
        def dp(i, j):
            if i > j: return 0
            parity = (j - i - len(piles)) % 2
            if parity == 1:  
                return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
            else:
                return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))

        return dp(0, len(piles) - 1) > 0