from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
    
        def canShip(capacity):
            total = 0
            day = 1

            for weight in weights:
                total += weight

                if total > capacity:
                    day += 1
                    total = weight  

                if day > days:  
                    return False
            return True 

        low = max(weights) - 1
        high = sum(weights)

        while high-low > 1:
            mid = low + (high - low) // 2

            if canShip(mid): 
                high = mid 

            else:
                low = mid 
        return high 