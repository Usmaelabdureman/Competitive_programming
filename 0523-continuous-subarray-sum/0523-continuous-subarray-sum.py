class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        rem = {0:-1}
        total = 0

        for i,val in enumerate(nums):
            total += val
            mod = total%k

            if mod not in rem:
                rem[mod] = i
            elif i - rem[mod] > 1:
                return True
        return False