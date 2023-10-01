class Solution(object):
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        lst=[]
        for i in range(len(nums)):
            if nums[i]==target:
                lst.append(i)
        return lst