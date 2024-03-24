# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        root_val = postorder.pop()
        root_idx = inorder.index(root_val)
        
        root = TreeNode(root_val)
        root.right = self.buildTree(inorder[root_idx + 1:], postorder)
        root.left = self.buildTree(inorder[:root_idx], postorder)
        
        return root
