class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        ans=0
        while l<len(nums):
            if nums[l]==0:
                l+=1
            else:
                r=l
                while (r<len(nums)-1) and nums[r+1]==1:
                    r+=1
                ans=max(ans,r-l+1)
                l=r+1
        return ans
                
                    
                
                
                
                
        