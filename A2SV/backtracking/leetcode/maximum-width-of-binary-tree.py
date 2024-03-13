from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        queue = deque([(root, 0)]) 
        max_width = 0

        while queue:
            _, level = queue[0]

            for i in range(len(queue)):
                node, pos = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * pos))
                if node.right:
                    queue.append((node.right, 2 * pos + 1))

            max_width = max(max_width, pos - level + 1)
        return max_width
