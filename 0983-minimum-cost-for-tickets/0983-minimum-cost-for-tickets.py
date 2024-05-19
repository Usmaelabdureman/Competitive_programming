class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        last_day = days[-1]
        dp = [0] * (last_day + 1)

        day_set = set(days)
        
        for day in range(1, last_day + 1):
            
            if day not in day_set:
                dp[day] = dp[day - 1]
                
            else:
                dp[day] = min(
                    dp[day - 1] + costs[0],
                    dp[max(0, day - 7)] + costs[1],
                    dp[max(0, day - 30)] + costs[2]
                )

        return dp[last_day]