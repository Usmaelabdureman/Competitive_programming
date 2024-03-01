class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        def backtrack(i = 0,path = []):

            result.add(tuple(sorted(path[:])))
            
            for choice in range(i , n):

                path.append(nums[choice])
                backtrack(choice + 1,path)
                path.pop()
                
        result = set()
        backtrack()
        return result