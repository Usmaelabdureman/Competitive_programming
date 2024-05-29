class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        @lru_cache(None)
        
        def dp(mask, i):
            if i == n: return 0
            return min(dp(mask ^ (1<<j), i + 1) + (nums1[i]^nums2[j]) for j in range(n) if mask & 1<<j)

        return dp((1<<n) - 1, 0)