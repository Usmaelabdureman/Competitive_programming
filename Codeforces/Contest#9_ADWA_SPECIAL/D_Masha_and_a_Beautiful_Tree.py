def solve(l, r, arr):
    if r - l == 1:
        return 0
    mid = (l + r) // 2
    mal = max(arr[l:mid])
    mar = max(arr[mid:r])
    ans = 0
    if mal > mar:
        ans += 1
        for i in range(mid - l):
            arr[l + i], arr[mid + i] = arr[mid + i], arr[l + i]
    return solve(l, mid, arr) + solve(mid, r, arr) + ans

def solve_case(m, arr):
    ans = solve(0, m, arr)
    if sorted(arr) == arr:
        return ans
    return -1

t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))
    print(solve_case(m, arr))
