class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators={'+', '-', '*', '/'}
        for token in tokens:
            if token in operators:
                second_elt = stack.pop()
                first_elt = stack.pop()
                if token == '+':
                    stack.append(first_elt  +  second_elt)
                elif token == '-':
                    stack.append(first_elt -   second_elt)
                elif token == '*':
                    stack.append(first_elt *   second_elt)
                else:
                    stack.append(int(first_elt /   second_elt))
            else:
                stack.append(int(token))
        return stack.pop()
