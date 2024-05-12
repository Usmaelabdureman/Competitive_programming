from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        low = 1
        high = 100
        
        def countMissing(n):
            missing_set = set(arr)
            cnt = 0
            for i in range(1, n):
                if i not in missing_set:
                    cnt += 1
            return cnt
            
        
        while low <= high:
            mid = (low + high)//2
            
            if countMissing(mid) < k:
                high = mid 
            else:
                low = mid 
        return high
    
test = [2,3,4,7,11]

k = 5
sol = Solution()
print(sol.findKthPositive(test, k))