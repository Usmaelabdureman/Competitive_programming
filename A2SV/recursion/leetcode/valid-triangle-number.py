class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums)

        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                k = bisect_left(nums, nums[i] + nums[j], lo=j + 1) - 1
                res += k - j
        return res