# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans_dict = {}
        def dfs(node,x,y):
            if node:
                if y not in ans_dict:
                    ans_dict[y] = []
                ans_dict[y].append([x,y,node.val])
                if node.left:
                    dfs(node.left,x+1,y-1)
                if node.right:
                    dfs(node.right,x+1,y+1)
        dfs(root,0,0)
        for i in ans_dict:
            ans_dict[i].sort()


        cols = sorted(ans_dict.items())

        res = []

        for x,y in cols:
            temp = [j[-1] for j in y]
            res.append(temp)
        return res