class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        dup = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                dup.append(index + 1)
            else:
                nums[index] *= -1
        return dup
