from math import ceil

def check(a, mid):
    n = len(a)
    local_min = a[0]
    for i in range(1, n - 1):
        x = max(a[i], a[i - 1])
        y = min(a[i], a[i - 1])

        # case one using the two min values
        if (ceil(local_min / 2) + ceil(a[i] / 2)) <= mid:
            return True

        # case two using i, i + 2
        elif (ceil((a[i - 1] + a[i + 1]) / 2)) <= mid:
            return True

        # case 3 using i, i + 1
        elif max(ceil(x / 2), ceil((x + y) / 3)) <= mid:
            return True

        # update local min
        local_min = min(local_min, a[i])

    return False


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    low, high, ans = 1, max(a), float('inf')
    a.append(1e7)
    while low <= high:
        mid = low + (high - low) // 2
        if check(a, mid):
            ans = min(ans, mid)
            high = mid - 1
        else:
            low = mid + 1

    print(ans)


if __name__ == "__main__":
    solve()
