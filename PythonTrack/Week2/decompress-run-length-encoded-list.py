class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(0,len(nums),2):
            freq,val=nums[i],nums[i+1] #For each pair, repeat the value val freq times and append it to the result list.
            ans.extend([val]*freq)
        return ans