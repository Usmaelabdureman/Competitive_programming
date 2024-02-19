class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []

        score = 0

        for char in s:
            if char == "(":
                stack.append(score)
                score = 0
            
            elif stack and char == ")":
                score = stack.pop() + max(2*score,1)
        return score

test = "(()(()))"
t =Solution()

print(t.scoreOfParentheses(test))
