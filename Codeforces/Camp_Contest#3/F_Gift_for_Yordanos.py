
string = input()

stack = []
ans = []

for ch in string:
    
    while stack and ch > stack[-1]:
        ans.append(stack.pop())
    else:
        stack.append(ch)

while stack:
    ans.append(stack.pop())
print("".join(ans))