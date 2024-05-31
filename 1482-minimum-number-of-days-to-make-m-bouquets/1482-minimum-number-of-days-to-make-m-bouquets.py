class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if m * k > len(bloomDay): return -1
        
        left, right = 1, max(bloomDay)
        
        while left < right:
            mid = (left + right) / 2
            flow = bouq = 0
            for num in bloomDay:
                flow = 0 if num > mid else flow + 1
                if flow >= k:
                    flow = 0
                    bouq += 1
                    if bouq == m: break
            if bouq == m:
                right = mid
            else:
                left = mid + 1
        return int(left)