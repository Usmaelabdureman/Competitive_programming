# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        res = []
        curr = ""
        def helper(node,curr):
            if node:
                curr += str(node.val)
                if not node.left and not node.right:
                    res.append(curr)
                if node.right:
                    helper(node.right,curr)
                if node.left:
                    helper(node.left,curr)
        helper(root,curr)
        ans = 0

        for num in res:
            ans += int(num)
        return ans
            