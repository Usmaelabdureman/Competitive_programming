#I solved it Using sliding window 
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        len_arr=len(nums)
        nums.sort()
        left=0
        maxFreq=0
        for right in range(len_arr):
            k+=nums[right]
            while k<nums[right]*(right-left+1):
                k-=nums[left]
                left+=1
            maxFreq=max(maxFreq,right-left+1)
        return maxFreq