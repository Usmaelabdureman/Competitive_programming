# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node, parent, depth, val):
            if not node:
                return
            if node.val == val:
                return parent, depth
            return dfs(node.left, node, depth + 1, val) or dfs(node.right, node, depth + 1, val)
        x_parent, x_depth = dfs(root, None, 0, x)
        y_parent, y_depth = dfs(root, None, 0, y)
        return x_depth == y_depth and x_parent != y_parent