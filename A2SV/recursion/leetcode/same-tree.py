# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and  q is None:
            return True

        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False

        # might be ignorant of tree use this
        # return str(p) == str(q)
        