class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        dup = []
        for num in nums:
            indx = abs(num) - 1
            if nums[indx] < 0:
                dup.append(indx + 1)
            else:
                nums[indx] *= -1
        return dup
