t = int(input())

for i in range(t):
    n = int(input())
    s = input()

    if s[0] not in ['m', 'M']:
        print("NO")
        continue

    j = 1
    while j < n and s[j] in ['m', 'M']:
        j += 1

    if j == n:
        print("NO")
        continue

    if s[j] not in ['e', 'E']:
        print("NO")
        continue

    j += 1
    while j < n and s[j] in ['e', 'E']:
        j += 1

    if j == n:
        print("NO")
        continue

    if s[j] not in ['o', 'O']:
        print("NO")
        continue

    j += 1
    while j < n and s[j] in ['o', 'O']:
        j += 1

    if j == n:
        print("NO")
        continue

    if s[j] not in ['w', 'W']:
        print("NO")
        continue

    j += 1
    if j != n:
        print("NO")
        continue

    print("YES")
