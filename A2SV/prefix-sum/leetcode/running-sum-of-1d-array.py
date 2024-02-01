class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # running_sum = [0]*n
        # running_sum[0] = nums[0]
        for i in range(1,n):
            # running_sum[i] = running_sum[i-1] + nums[i]
            nums[i] += nums[i-1]
        return nums