class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans=0
        curSum=0
        prevSum={0:1}
        for i in nums:
            curSum+=i
            diff=curSum-k
            ans+=prevSum.get(diff,0)
            prevSum[curSum]=1+prevSum.get(curSum,0)
        return ans