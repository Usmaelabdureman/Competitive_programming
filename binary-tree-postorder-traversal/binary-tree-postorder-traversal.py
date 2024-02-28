# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        curr = TreeNode(root)
        if(root == None): return []
#         visited=[]
#         stack = []
#         stack.append(root)

#         while len(stack) > 0:
#             parent = stack.pop()
            
#             if parent.left : stack.append(parent.left)
#             if parent.right: stack.append(parent.right)
#             visited.append(parent.val)

#         return visited
        
        # postOrder = []

        # def dfs(node):
        #     if node is None:
        #         return 
        #     dfs(node.left)
        #     dfs(node.right)
        #     postOrder.append(node.val)
        # dfs(root)

        # return postOrder
        
        if root is None:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]