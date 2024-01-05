class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur=0
        for i in range(k):
            cur+=nums[i]
        res=cur
        for j in range(k,len(nums)):
            cur+=nums[j]
            cur-=nums[j-k]
            res=max(res,cur)
        return res/k