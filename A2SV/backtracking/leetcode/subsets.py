class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def backtrack(i = 0,path = []):

            result.add(tuple(path[:]))
            
            for choice in range(i , n):
                path.append(nums[choice])
                print(path)
                backtrack(choice + 1,path)
                path.pop()

        result = set()
        backtrack()
        return result