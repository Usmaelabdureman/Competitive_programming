# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
    
        # Initialize a queue for BFS traversal
        queue = [root]
        is_null_node = False
        
        # Traverse the tree level-by-level
        while queue:
            node = queue.pop(0)
            
            # If we have encountered a null node, set the flag
            if not node:
                is_null_node = True
            
            # If a non-null node has been encountered after a null node, the tree is not complete
            elif is_null_node:
                return False
            
            # Add the left and right child to the queue
            else:
                queue.append(node.left)
                queue.append(node.right)
        
        # If we reach here, the tree is complete
        return True
        


   
