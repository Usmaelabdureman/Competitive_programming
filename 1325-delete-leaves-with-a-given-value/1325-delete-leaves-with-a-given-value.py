# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # Base case
        if root is None:
            return None
        
        # 1. Visit the left children
        root.left = self.removeLeafNodes(root.left, target)
        
        # 2. Visit the right children
        root.right = self.removeLeafNodes(root.right, target)
        
        # 3. Check if the current node is a leaf node and its value equals target
        if root.left is None and root.right is None and root.val == target:
            # Delete the node by returning None to the parent, effectively disconnecting it
            return None
        
        # Keep it untouched otherwise
        return root