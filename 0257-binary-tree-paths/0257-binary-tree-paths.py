# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            if not node:
                return

            path.append(str(node.val))

            if not node.left and not node.right:
                # Leaf node, add the path to the result list
                result.append("->".join(path))

            if node.left:
                dfs(node.left, path)

            if node.right:
                dfs(node.right, path)

            # Backtrack: Remove the current node from the path
            path.pop()

        result = []
        dfs(root, [])
        return result
