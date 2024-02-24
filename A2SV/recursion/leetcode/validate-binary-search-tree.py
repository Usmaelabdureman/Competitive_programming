# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            # Condition 1 when node is None
            
            if not node:
                return True
        

            if not (left < node.val < right):
                return False
           

            checkleft = dfs(node.left, left, node.val)
            checkright = dfs(node.right, node.val, right)
            return checkleft and checkright
            

        return dfs(root, float("-inf"), float("inf"))
        