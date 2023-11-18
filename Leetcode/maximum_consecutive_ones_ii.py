"""
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

 

Example 1:

Input: nums = [1,0,1,1,0]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
 

Follow up: What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

Algorithm
What if the question says that it can be flipped k times?

It is best to use a general solution to deal with this kind of problem. A window [left,right] can be maintained to hold at least k zeros. When it encounters 0, it accumulates the number of zero, and then judges if the number of 0 is greater than k at this time, then shifts the left boundary left to the right, and if the removed nums[left] is 0, then zero decrements by 1. If it is not greater than k, use the number of digits in the window to update res.

Follow up
The above method cannot be used in the case of follow up, because nums[left] needs to access the previous number. We can save all the positions of 0 we encountered in a queue, so that we know where to move when we need to move left.


    """
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        flip=1
        left=0
        res=0
        zeros=0
        for right in range(len(nums)):
            if nums[right]==0:
                zeros+=1
            while zeros>flip:
                if nums[left]==0:
                    zeros-=1
                left+=1
            res=max(res,right-left+1)
        return res
    
# Using sliding window
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0 # count of consecutive 1's
        max_count=0
        prev_count=0 # count of consecutive 1's before the current 0
        for num in nums:
            if num==1:
                count+=1
                prev_count+=1
            else:
                count=prev_count+1
                prev_count=0
        max_count=max(max_count,count)
        if num == 0 and prev_count == 0:
            count=0
            prev_count=0
        return max_count
    
if __name__ == "__main__":
    test_case_1 = [1,0,1,1,0]
    
    print(Solution().findMaxConsecutiveOnes(test_case_1))
    test_case_2 = [1,0,1,1,0,1]
    
    print(Solution().findMaxConsecutiveOnes(test_case_2))
