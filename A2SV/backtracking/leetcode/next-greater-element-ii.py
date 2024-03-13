class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % n]:
                stack.pop()
            res[i % n] = -1 if not stack else nums[stack[-1]]
            stack.append(i % n)

        return res
