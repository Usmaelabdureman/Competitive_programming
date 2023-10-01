t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ones_count = sum(a)
    zeros_count = n - ones_count
    first_one_index = a.index(0)
    last_one_index = n - a[::-1].index(1) - 1
    ans = min(zeros_count - first_one_index, last_one_index - ones_count)
    
    print(ans)
