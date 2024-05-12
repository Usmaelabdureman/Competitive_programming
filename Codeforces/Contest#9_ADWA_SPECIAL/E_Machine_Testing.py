import sys
from math import ceil, inf

def solve():
    n = int(input())
    h = list(map(int, input().split()))
    power = list(map(int, input().split()))

    stack = [(inf, power[0])]
    ans = 0

    for i in range(1, n):
        time_elapsed = 0

        while h[i] - (stack[-1][0] - time_elapsed) * stack[-1][-1] > 0:
            t, p = stack.pop()
            h[i] -= (t - time_elapsed) * p
            time_elapsed += (t - time_elapsed)

        time_elapsed += ceil(h[i] / stack[-1][-1])
        stack.append((time_elapsed, power[i]))
        ans = max(ans, time_elapsed)

    return ans

def main():
    t = int(input())
    for _ in range(t):
        print(solve())

if __name__ == "__main__":
    main()