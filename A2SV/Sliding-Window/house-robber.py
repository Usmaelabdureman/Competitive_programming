class Solution:
    def rob(self, nums: List[int]) -> int:
        count1=0
        count2=0
        for i in nums:
            count1, count2 = count2, max(i + count1, count2)
        return count2