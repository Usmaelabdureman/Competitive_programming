class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref_sum = sum(nums)
        leftSum = 0
        ans = [0]*n
       

        for i in range(n):
            pref_sum -= nums[i]
            ans[i] = abs(leftSum-(nums[i]*i)) + abs(pref_sum -nums[i]* (n-1-i))
            leftSum += nums[i]
            
            
        return ans