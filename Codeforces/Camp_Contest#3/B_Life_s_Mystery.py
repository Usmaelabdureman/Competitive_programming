string = input()

stack = []
        
for ch in string:
    if stack and ch == stack[-1]:
        stack.pop()
    else:
        stack.append(ch)
    
print("".join(stack))
