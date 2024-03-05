class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        to_remove = set()

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)

  
        to_remove.update(stack)

        result = []
        for i, char in enumerate(s):
            if i not in to_remove:
                result.append(char)

        return ''.join(result)
