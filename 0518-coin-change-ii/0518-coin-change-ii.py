class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        
        def dp(i,amount):
            
            if amount == 0:
                return 1
            if i == len(coins) or amount < 0:
                return 0
            
            return dp(i,amount - coins[i]) + dp(i+1, amount)
        return dp(0,amount)