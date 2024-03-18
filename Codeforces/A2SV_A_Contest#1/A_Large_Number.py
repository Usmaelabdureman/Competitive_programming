def solve():
    n, d = map(int, input().split())
    s = input().strip()
    for i in range(n):
        if int(s[i]) - int('0') >= d:
            print(s[i], end='')
        else:
            print(d, end='')
            for j in range(i, n):
                print(s[j], end='')
            print()
            return
    print(d)

t = int(input())
for _ in range(t):
    solve()

