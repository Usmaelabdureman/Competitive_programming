class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return 0
        else:

            i=0
            for value in range(len(nums)):
                if nums[value]!=val:
                    nums[i]=nums[value]
                    i+=1
            return i