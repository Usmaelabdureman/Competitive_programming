class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_elt = max(nums)

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
            
        @cache
        def dp(n):
            if n < 0:
                return 0
            return max(dp(n - 1), dp(n - 2) + n * freq[n]) 
        return dp(max_elt)