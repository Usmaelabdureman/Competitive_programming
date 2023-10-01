# Time Complexity: O(nlog⁡n) where n is the length of people.

# Space Complexity: O(n)

# Some extra space is used when we sort people in place. The space complexity of the sorting algorithm depends on which sorting algorithm is used; the default algorithm varies from one language to another.

# In python, the sort method sorts a list using the Timsort algorithm, which is a combination of Merge Sort and Insertion Sort and uses O(n) additional space.

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left=0
        right=len(people)-1
        result=0
        while left<=right:
            result+=1
            if people[left]+people[right]<=limit:
                left+=1
            right-=1
        return result