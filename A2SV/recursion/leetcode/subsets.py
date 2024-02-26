class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(i,path):
            ans.append(path[:])
            for i in range(i,n):
                path.append(nums[i])
                dfs(i+1,path)
                path.pop()

        nums.sort()
        ans = []
        n = len(nums)
        dfs(0,[])
        return ans

        # ans = [[]]
        # if not nums:
        #     return [[]]
        # for num in nums:
        #     ans += [subset + [num] for subset in ans]
        # return ans