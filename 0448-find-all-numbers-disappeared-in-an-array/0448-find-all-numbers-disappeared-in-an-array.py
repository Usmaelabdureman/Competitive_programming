class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        n = len(nums)
        ans = []
        
        
        for i in range(1,n+1):
            if i not in set_nums:
                ans.append(i)
        return ans