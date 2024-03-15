class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        low, high = 0, n - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            target = n - mid
                
            if citations[mid] < target:
                low = mid + 1
            elif citations[mid] > target:
                high = mid - 1
            else:
                return target
        return n - low
