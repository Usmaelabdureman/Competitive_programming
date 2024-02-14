class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x : x[0]-x[1])
        
        ans = 0
        n = len(costs)//2
        
        i = 0
        
        while i < n:
            
            ans += costs[i][0] 
            ans += costs[n+i][1]
            i += 1
        return ans