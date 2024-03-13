 

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input()))
    total = 0
    curr_sum = 0
    d = {0:1}
    for i in range(n):
        curr_sum += a[i]
        if curr_sum - i - 1 in d:
            total += d[curr_sum - i - 1]
        if curr_sum - i - 1 in d:
            d[curr_sum - i - 1] += 1
        else:
            d[curr_sum - i - 1] = 1
    print(total)
    
 