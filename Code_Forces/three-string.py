t = int(input())
for _ in range(t):
    a = input().strip()
    b = input().strip()
    c = input().strip()
    possible = all(c[i] == a[i] or c[i] == b[i] for i in range(len(a)))
    same = a == b
    if possible and not same:
        print("YES")
    else:
        print("NO")


