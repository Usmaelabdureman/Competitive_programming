class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                subString = ""
                while stack[-1] != "[":
                    subString = stack.pop() + subString
                stack.pop()
                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier
                stack.append(int(multiplier) * subString)
        return [] if stack==[] else "".join(stack)
