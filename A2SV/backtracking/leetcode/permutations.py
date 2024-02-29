import sys

sys.setrecursionlimit(1<<30)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(used =set(),path = []):
            if len(path) == len(nums):
                permutations.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in used:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtrack(used,path)
                    path.pop()
                    used.remove(nums[i])
        permutations = []
        backtrack()
        return permutations