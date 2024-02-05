t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    min_num=min(a)
    max_num=max(a)
    Sum=sum(a)-min_num+max_num
    if Sum<= m-n:
        print('YES')
    else:
        print('NO')