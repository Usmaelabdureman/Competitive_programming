class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(openP = 0,closeP = 0):
            if openP == closeP ==n:
                res.append("".join(parentheses))
                return
            if openP < n:
                parentheses.append("(")
                backtrack(openP+1,closeP)
                parentheses.pop()
            if closeP < openP:
                parentheses.append(")")
                backtrack(openP,closeP+1)
                parentheses.pop()
        parentheses=[]
        res=[]
        backtrack()
        return res
        