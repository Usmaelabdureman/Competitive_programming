from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_values = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                if left_to_right:
                    level_values.append(node.val)
                else:
                    level_values.insert(0, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_values)
            left_to_right = not left_to_right

        return result
