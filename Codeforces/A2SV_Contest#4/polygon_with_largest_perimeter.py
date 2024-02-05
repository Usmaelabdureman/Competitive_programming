from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n=len(nums)
        for i in range(len(nums) - 2):
            if nums[i] < sum(nums[i+1:n]):
                return sum(nums[i:n])
        return -1

# our input [5,5,5], [1,12,1,2,5,50,3] ,[5,5,50] 
test = Solution()
print(test.largestPerimeter([5,5,5]))
print(test.largestPerimeter([1,12,1,2,5,50,3]))
print(test.largestPerimeter([5,5,50]))