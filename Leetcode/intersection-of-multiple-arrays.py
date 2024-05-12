"""
Intersection of Multiple Arrays
User Accepted:8227
User Tried:8525
Total Accepted:8430
Total Submissions:12757
Difficulty:Easy
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
 

Example 1:

Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: 
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
Example 2:

Input: nums = [[1,2,3],[4,5,6]]
Output: []
Explanation: 
There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].
 

Constraints:

1 <= nums.length <= 1000
1 <= sum(nums[i].length) <= 1000
1 <= nums[i][j] <= 1000
All the values of nums[i] are unique.

Python3	
1
class Solution:
2
    def intersection(self, nums: List[List[int]]) -> List[int]:
3
        """


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # Approach 1: Using set intersection
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)
        # return list(set(nums[0]).intersection(*nums[1:]))
        
        # Approach 2: Using Counter
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)
        # return list((Counter(nums[0]) & Counter(nums[1])).elements())
        
        # Approach 3: Using reduce
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)
        # return list(reduce(lambda x, y: x & y, map(Counter, nums)).elements())
        
        # Approach 4: Using reduce and set intersection
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)
        return list(reduce(set.intersection, map(set, nums)))
        
        # Approach 5: Using reduce and Counter
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)
        # return list(reduce(lambda x, y: x & y, map(Counter, nums)).elements())
        
        # Approach 6: Using reduce and Counter
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)
        # return list(reduce(lambda x, y: x & y, map(Counter, nums)).elements())
        
        # Approach 7: Using reduce and Counter
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)
        # return list(reduce(lambda x, y: x & y, map(Counter, nums)).elements())
        
        # Approach 8: Using reduce and Counter
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)
        # return list(reduce(lambda x, y: x & y, map(Counter, nums)).elements())
        
        # Approach 9: Using reduce and Counter
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)
        # return list(reduce(lambda x, y: x & y, map(Counter, nums)).elements())
        
        # Approach 10: Using reduce and Counter
        #