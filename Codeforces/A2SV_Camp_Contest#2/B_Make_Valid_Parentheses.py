brak = input()

stack = []
count = 0

for char in brak:
    if char == '(':
        stack.append(char)
    elif char == ')' and stack:
        stack.pop()
        count += 2

print(count)
