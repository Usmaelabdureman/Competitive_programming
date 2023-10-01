class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack, buffer = [], ''
        for char in s:
            if char!=')':
                stack.append(char)               
            else:
                buffer = ''
                while stack[-1]!='(':
                    buffer+= stack.pop()
                stack.pop()
                for ss in buffer:
                    stack.append(ss)
        return ''.join(stack)