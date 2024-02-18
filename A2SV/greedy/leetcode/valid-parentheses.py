class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {')': '(', '}': '{', ']': '['}
        
        for c in s:
            if c in parentheses.values():
                stack.append(c)
            elif c in parentheses.keys():
                if not stack or parentheses[c] != stack.pop():
                    return False
            else:
                return False
        return not stack