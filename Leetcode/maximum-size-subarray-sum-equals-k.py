from typing import List
# class Solution:
#     def maxSubArrayLen(self, nums: List[int], k: int) -> int:
#         maxLen=0
#         for i in range(len(nums)):
#             Sum=0
#             for j in range(i, len(nums)):
#                 Sum+=nums[j]
#                 if Sum==k:
#                     maxLen=max(maxLen, j-i+1)
#         return maxLen
    
    
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        cnt={0:-1}
        maxLen=0
        
        Sum=0
        for i,v in enumerate(nums):
            Sum+=v
            if Sum-k in cnt:
                maxLen=max(maxLen, i-cnt[Sum-k])
            if Sum not in cnt:
                cnt[Sum]=i
        return maxLen
        
if __name__ == "__main__":
    test1=Solution()
    print(test1.maxSubArrayLen([1,-1,5,-2,3], 3))