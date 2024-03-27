class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        missing = []
        
        for i in range(1,10**5):
            if i not in set(arr):
                missing.append(i)
                if len(missing) > k:
                    break
        # print(missing)
        return missing[k-1]
            