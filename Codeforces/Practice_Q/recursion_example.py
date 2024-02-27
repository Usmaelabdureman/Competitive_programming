# ans = 0
# def fact(n):
#     global ans
    
#     if n == 1:
#         return 1
#     ans += 1
#     return n*fact(n-1)
# print(fact(5))
# print(ans)

def divideInBuckets(i, picked) -> int:
    if i >= len(picked):
        return 0
    notPick = divideInBuckets(i+1,picked)
    
    picked.append(picked[i])
    
    pick = divideInBuckets(i+1,picked)
    
    return pick + notPick

print(divideInBuckets(3,[3,4,5,6,6]))