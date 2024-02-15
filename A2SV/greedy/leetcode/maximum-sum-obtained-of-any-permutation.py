class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        n = len(nums)
        MOD = 10**9 + 7

        diff_array = [0] * (n + 1)
        for l, r in requests:
            diff_array[l] += 1
            diff_array[r + 1] -= 1

        pref_diff = list(accumulate(diff_array))
        pref_diff.sort(reverse=True)

        nums.sort(reverse=True)

        res = 0
        for i in range(n):
            res += (nums[i] * pref_diff[i])

        return res % MOD
