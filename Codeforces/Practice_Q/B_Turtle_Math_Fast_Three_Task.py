import math
t = int(input())

for _ in range(t):
    n = int(input())
    
    a = list(map(int,input().split()))
    
    a_sum = sum(a)

    ans = []
    
    if a_sum%3 == 0:
        ans.append(0)
    else:
        r = 0
        while a_sum >= 1:
            r += a_sum%3
            a_sum /= 3
        if math.ceil(r) in a:
            ans.append(1)
        else:
            ans.append(int(min((3*math.ceil(r)) - a_sum,(3*math.floor(r)) - a_sum)))
    r = 0
    while a_sum >= 1:
        r += a_sum % 3
        a_sum //= 3
    if math.ceil(r) in a:
        ans.append(1)
    else:
        ans.append(int(min((3 * math.ceil(r)) - a_sum, (3 * math.floor(r)) - a_sum)))
    print(*ans)