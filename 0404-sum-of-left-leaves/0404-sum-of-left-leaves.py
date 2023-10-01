# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def is_leaf(node):
            return node and not node.left and not node.right

        def dfs(node):
            if not node:
                return 0

            if is_leaf(node.left):
                left_sum = node.left.val
            else:
                left_sum = dfs(node.left)

            right_sum = dfs(node.right)

            return left_sum + right_sum

        if not root:
            return 0

        return dfs(root)
