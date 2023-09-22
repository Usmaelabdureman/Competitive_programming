class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses=[]
        res=[]
        def backtrack(openP,closeP):
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
        backtrack(0,0)
        return res
        