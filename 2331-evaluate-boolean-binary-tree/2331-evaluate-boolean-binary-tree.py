class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            # Handles the case for leaf nodes.
            return root.val != 0

        # Store the evaluations for the left subtree and right subtree.
        evaluate_left_subtree = self.evaluateTree(root.left)
        evaluate_right_subtree = self.evaluateTree(root.right)
        if root.val == 2:
            evaluate_root = evaluate_left_subtree or evaluate_right_subtree
        else:
            evaluate_root = evaluate_left_subtree and evaluate_right_subtree

        return evaluate_root