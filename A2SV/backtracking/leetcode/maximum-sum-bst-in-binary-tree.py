# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0

        def isBST(node, left, right):
            nonlocal max_sum

            if not node:
                return 0, float('inf'), float('-inf')

            left_sum, left_min, left_max = isBST(node.left, left, node.val)
            right_sum, right_min, right_max = isBST(node.right, node.val, right)

            if left_max < node.val < right_min:
                total = node.val + left_sum + right_sum
                max_sum = max(max_sum, total)
                return total, min(left_min, node.val), max(right_max, node.val)
            return 0, float('-inf'), float('inf')

        isBST(root, float('-inf'), float('inf'))
        return max_sum
