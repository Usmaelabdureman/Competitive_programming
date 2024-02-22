# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delete = set(to_delete)
        result = []

        def forest(node,delet):
            if not node:
                return None
            
            node.right = forest(node.right,delet)
            node.left = forest(node.left,delet)

            if node.val in delete:
                if node.right: result.append(node.right)
                if node.left : result.append(node.left)
                return None
            return node
        

        root = forest(root,delete)
        if root:
            result.append(root)
            
        return result
