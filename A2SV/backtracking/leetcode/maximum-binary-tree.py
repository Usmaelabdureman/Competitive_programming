# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def buildTree(half_nums):

            if len(half_nums) == 0:
                return None
            
            pivot = max(half_nums)
            half = half_nums.index(pivot)


            left = half_nums[:half]
            right = half_nums[half+1:]

            # print(pivot)
            # print(left)
            # print(right)
            return TreeNode(pivot, buildTree(left), buildTree(right))
        return buildTree(nums)
