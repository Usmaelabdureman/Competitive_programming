from typing import List

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        max_val = float('-inf')

        # Calculate prefix array
        for i in range(n):
            max_val = max(max_val, nums[i])
            pref[i] = nums[i] + max_val

        ans = [0] * n
        ans[0] = pref[0]

    
        for i in range(1, n):
            ans[i] = pref[i] + ans[i - 1]

        return ans
