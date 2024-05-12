class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        pref_sum = [nums[0]]
        
        for i in range(1, len(nums)):
            pref_sum.append(pref_sum[len(pref_sum)-1] ^ nums[i])
       
        comparison = 2 ** maximumBit
        ans = []
        
        for i in range(len(pref_sum)-1, -1, -1):

            curr_res = pref_sum[i]
    
            res = curr_res ^ (comparison - 1)
            ans.append(res)
        return ans
