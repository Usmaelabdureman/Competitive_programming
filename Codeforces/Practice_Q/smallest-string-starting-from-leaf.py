# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallestString = ""

        def dfs(node,currentString):
            nonlocal smallestString
            
            if node is None:
                return 
            
            currentString = chr(node.val + 97) + currentString
            print(currentString)
            print(f"small = {smallestString}")
            if not root.left and not root.right:
                if currentString < smallestString or not smallestString:
                    smallestString  = currentString
            if node.left:
                dfs(node.left,currentString)
                
            if node.right:
                dfs(node.right,currentString)
        dfs(root,"")
        
        return smallestString
