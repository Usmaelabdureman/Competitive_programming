class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit_stock = 0
        profit_coold = 0
        profit_nostock = -prices[0]
        
        for price in prices[1:]:
            
            old_prof_stock = profit_stock
            old_prof_coold = profit_coold
            old_prof_nostock = profit_nostock

            profit_stock = old_prof_coold
            profit_coold = max(old_prof_coold, old_prof_nostock + price)
            profit_nostock = max(old_prof_nostock, old_prof_stock - price)

        return profit_coold