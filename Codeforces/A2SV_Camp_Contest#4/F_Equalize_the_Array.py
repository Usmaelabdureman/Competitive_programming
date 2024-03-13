def solve():
    n = int(input())
    cnt = {}
    
    x = list(map(int,(input().split())))
    
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1
    
    
    groupedByCnt = {}
    for x, y in cnt.items():
        if y in groupedByCnt:
            groupedByCnt[y] += 1
        else:
            groupedByCnt[y] = 1

    res = n
    left = 0
    right = n
    rightCnt = len(cnt)
    for x, y in groupedByCnt.items():
        res = min(res, left + right - rightCnt * x)
        left += x * y
        right -= x * y
        rightCnt -= y
    print(res)

tests = int(input())
for _ in range(tests):
    solve()

# from collections import defaultdict
# test = int(input())

# for _ in range(test):
#     n = int(input())
    
#     arr = list(map(int,input().split()))
    
#     freq = defaultdict(int)
    
  

#     for num in arr:
#         freq[num] += 1
  
#     print(freq)
    
    