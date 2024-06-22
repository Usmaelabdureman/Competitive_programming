class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curSum = ans = 0
        prevSum={0:1}
        for i in range(len(nums)):
            
            curSum += nums[i] % 2
            diff=curSum - k
            
            if diff in prevSum:
                ans += prevSum.get(diff,0)
                
            prevSum[curSum]= 1+prevSum.get(curSum,0)
        return ans