
s = input()

stack = []
count = 0

for char in s:
    if stack and  stack[-1] == char:
        stack.pop()
        count += 1
    stack.append(char)
print("Yes") if count%2 else print("No")
    