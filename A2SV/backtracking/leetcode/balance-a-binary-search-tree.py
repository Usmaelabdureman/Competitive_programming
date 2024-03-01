# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def getInOrder(node):
            if node:
                getInOrder(node.left)
                res.append(node.val)
                getInOrder(node.right)
        res = []
        getInOrder(root)

        def buildTree(arr):

            if len(arr) == 0:
                return None
            
            pivot = arr[len(arr)//2]
            half = len(arr)//2


            left = arr[:half]
            right = arr[half+1:]

            # print(pivot)
            # print(left)
            # print(right)
            return TreeNode(pivot, buildTree(left), buildTree(right))

        return buildTree(res)