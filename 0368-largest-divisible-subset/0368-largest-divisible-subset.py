class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [0] * n
        parent = [0] * n
        max_index, max_length = 0, 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n): # note: not i+1, for i==j length is 1
                if nums[j] % nums[i] == 0 and dp[i] < 1 + dp[j]:
                    dp[i] = 1 + dp[j]
                    parent[i] = j

                    if dp[i] > max_length:
                        max_length = dp[i]
                        max_index = i
        res = []
        for _ in range(max_length):
            res.append(nums[max_index])
            max_index = parent[max_index]

        return res