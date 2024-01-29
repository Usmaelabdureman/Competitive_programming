class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0]*(n)
        rev_num =reversed(nums)
        suf_sum = list(accumulate(rev_num))
        suf_sum.reverse()
        
        for i in range(n):
            prefix_sum[i] = prefix_sum[i-1]+nums[i]
        
        for idx in range(n):
            if prefix_sum[idx] == suf_sum[idx]:
                return idx
        return -1