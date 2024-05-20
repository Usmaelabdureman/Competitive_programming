class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dp = defaultdict(int)
        for x in arr:
            dp[x] = dp[x - difference] + 1
        return max(dp.values())