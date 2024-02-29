# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []
        def inOrder(node):
            if node:
                inOrder(node.left)
                res.append(node.val)
                inOrder(node.right)
        inOrder(root)
        l = res.index(low)
        r = res.index(high)

        ans = sum(res[l:r+1])
        return ans
        