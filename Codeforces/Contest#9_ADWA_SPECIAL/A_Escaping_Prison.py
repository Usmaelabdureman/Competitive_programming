
t = int(input())

def check(n, h, blankets):
    total_height = 0
    for blanket in blankets:
        if blanket[0 ] >= h or blanket[1] >= h:
            return "YES"
        total_height += max(blanket)
        if total_height >= h:
            return "YES"
    return "NO"

for _ in range(t):
    n, h = map(int, input().split())
    total_height = 0
    blankets = [list(map(int, input().split())) for _ in range(n)]
    print(check(n, h, blankets))