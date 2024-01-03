class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        else:
            length=1
            prev=nums[0]
            idx=1
            for i in range (1,len(nums)):
                if nums[i]!=prev:
                    length+=1
                    prev=nums[i]
                    nums[idx]=nums[i]
                    idx+=1
            return length
        
                
       