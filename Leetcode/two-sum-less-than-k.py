from typing import List
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        max_sum =-1
        while left < right:
            cur_sum=nums[left]+nums[right] 
            if cur_sum >k:
                right-=1
            elif cur_sum < k:
                max_sum=max(max_sum,cur_sum)
                left+=1
        return max_sum
    
if __name__=="__main__":
    test1=[34,23,1,24,75,33,54,8]
    k=60
    print(Solution().twoSumLessThanK(test1,k))
    
    test2=[10,20,30]
    k2=15
    print(Solution().twoSumLessThanK(test2,k2))
                
                
                
             
            
        