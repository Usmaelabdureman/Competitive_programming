
# def backtrack(i=0,cum=0):
    
#     if str(cum)[-1] == '3':
#         ans.append(cum)
#         return
#     j = i+1
#     for k in range(j+1,n):
        
#         cum += (last_digit[i] + last_digit[j]+last_digit[k])
#         backtrack(i + 1,cum)
#         cum -= (last_digit[i] + last_digit[j]+last_digit[k])
#         j += 1
        
# test  = int(input())

# for _ in range(test):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     last_digit = [int(str(i)[-1] )for i in arr]
#     ans = []
#     backtrack()
    
#     if ans:
#         print("YES")
#     else:
#         print("NO")

def solve():
    n = int(input())
    cnt = [0] * 10
    numbers = list(map(int, input().split()))

    for x in numbers:
        cnt[x % 10] += 1

    v = []
    for i in range(10):
        for j in range(min(cnt[i], 3)):
            v.append(i)

    m = len(v)
    for i in range(m):
        for j in range(i + 1, m):
            for k in range(j + 1, m):
                if (v[i] + v[j] + v[k]) % 10 == 3:
                    print("YES")
                    return
    print("NO")

def main():
    tt = int(input())
    for _ in range(tt):
        solve()

if __name__ == "__main__":
    main()
