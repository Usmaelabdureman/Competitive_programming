"""
1918. Kth Smallest Subarray Sum
Level
Medium

Description
Given an integer array nums of length n and an integer k, return the k-th smallest subarray sum.

A subarray is defined as a non-empty contiguous sequence of elements in an array. A subarray sum is the sum of all elements in the subarray.

Example 1:

Input: nums = [2,1,3], k = 4

Output: 3

Explanation: The subarrays of [2,1,3] are:

[2] with sum 2
[1] with sum 1
[3] with sum 3
[2,1] with sum 3
[1,3] with sum 4
[2,1,3] with sum 6
Ordering the sums from smallest to largest gives 1, 2, 3, 3, 4, 6. The 4th smallest is 3.

Example 2:

Input: nums = [3,3,5,5], k = 7

Output: 10

Explanation: The subarrays of [3,3,5,5] are:

[3] with sum 3
[3] with sum 3
[5] with sum 5
[5] with sum 5
[3,3] with sum 6
[3,5] with sum 8
[5,5] with sum 10
[3,3,5], with sum 11
[3,5,5] with sum 13
[3,3,5,5] with sum 16
Ordering the sums from smallest to largest gives 3, 3, 5, 5, 6, 8, 10, 11, 13, 16. The 7th smallest is 10.

Constraints:

n == nums.length
1 <= n <= 2 * 10^4
1 <= nums[i] <= 5 * 10^4
1 <= k <= n * (n + 1) / 2
Solution
Use binary search. The maximum subarray sum is the sum of all elements in nums and the minimum subarray sum is the minimum element in nums. Initialize high and low as the maximum subarray sum and the minimum subarray sum. Each time let mid be the mean of high and low and count the number of subarrays that have sum less than or equal to mid, and adjust high and low accordingly. Finally the k-th smallest subarray sum can be obtained.

To count the number of subarrays that have sum less than or equal to mid, use sliding window over nums and for each index, count the number of subarrays that end at the index with sum less than or equal to mid.
    """

from bisect import bisect_left
from typing import List
class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        low, high = min(nums), sum(nums)
        while low < high:
            mid = (low + high) // 2
            if self.countSubarrays(nums, mid) < k:
                low = mid + 1
            else:
                high = mid
        return low 
    
    def countSubarrays(self, nums, target):
        start = end = Sum = count = 0
        while end < len(nums):
            Sum += nums[end]
            while Sum > target:
                Sum -= nums[start]
                start += 1
            count += end - start + 1
            end += 1
        return count
        
        
if __name__=="__main__":
    test_case_1= [2,1,3]
    k=4
    print(Solution().kthSmallestSubarraySum(test_case_1,k))
    test_case_2 = [3,3,5,5]
    k = 7
    print(Solution().kthSmallestSubarraySum(test_case_2,k))
            
        