
n = int(input())
wormss = list(map(int, input().split()))
m = int(input())

q = list(map(int, input().split()))

pref_sum = []
cur = 0

for i in range(n):
    cur += wormss[i]
    pref_sum.append(cur)
    
# print(pref_sum)

pairs = []
pairs.append([1, wormss[0]])
for i in range(1, n):
    pairs.append([pref_sum[i - 1] + 1, pref_sum[i]])
    
# print(pairs)

ans = []

for quer in q:
          
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        pair = pairs[mid]
        
        if pair[0] <= quer <= pair[1]:
            ans.append(mid + 1)
            break
        
        elif pair[0] > quer:
            high = mid - 1
        else:
            low = mid + 1
              
for i in ans:
    print(i)
