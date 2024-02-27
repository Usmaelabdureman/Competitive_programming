# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # #  My approach 
        # counter = defaultdict(int)
        
        # def dfs(node):
        #     if node:
        #         counter[node.val] += 1
        #         dfs(node.left)
        #         dfs(node.right)
        # dfs(root)

        # maxfreq = max(counter.values())
        # res = []
        # for k,v in counter.items():
        #     if v == maxfreq:
        #         res.append(k)
        # return res

        # # Approach two using  stack
        # counter = defaultdict(int)
        # stack = [root]
        
        # while stack:
        #     node = stack.pop()
        #     counter[node.val] += 1
            
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        
        # max_freq = max(counter.values())
        
        # res = []
        # for key in counter:
        #     if counter[key] == max_freq:
        #         res.append(key)
        
        # return res

        # # Approach three 
        # def dfs(node, values):
        #     if not node:
        #         return
        #     dfs(node.left, values)
        #     values.append(node.val)
        #     dfs(node.right, values)
            
        # values = []
        # dfs(root, values)
        
        # max_streak = 0
        # curr_streak = 0
        # curr_num = 0
        # ans = []
        
        # for num in values:
        #     if num == curr_num:
        #         curr_streak += 1
        #     else:
        #         curr_streak = 1
        #         curr_num = num
                
        #     if curr_streak > max_streak:
        #         ans = []
        #         max_streak = curr_streak

        #     if curr_streak == max_streak:
        #         ans.append(num)

        # return ans

        #  Approach four BFS
        counter = defaultdict(int)
        queue = deque([root])

        while queue:
            node = queue.popleft()
            counter[node.val] += 1
            if node.left :
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        maxFreq = max(counter.values())

        res = []
        for k, v in counter.items():
            if v == maxFreq:
                res.append(k)
        return res

        #  Approach five Morris Traversal

