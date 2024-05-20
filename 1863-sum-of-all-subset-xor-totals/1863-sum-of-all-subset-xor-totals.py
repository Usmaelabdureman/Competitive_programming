class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        xor_total = 0
        for num in nums:
            xor_total |= num
        return xor_total << (len(nums)-1)
            