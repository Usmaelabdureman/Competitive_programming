"""
Same Differences
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given an array a
 of n
 integers. Count the number of pairs of indices (i,j)
 such that i<j
 and aj−ai=j−i
.

Input
The first line contains one integer t
 (1≤t≤104
). Then t
 test cases follow.

The first line of each test case contains one integer n
 (1≤n≤2⋅105
).

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤n
) — array a
.

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.

Output
For each test case output the number of pairs of indices (i,j)
 such that i<j
 and aj−ai=j−i
.

Example
inputCopy
4
6
3 5 1 4 6 6
3
1 2 3
4
1 3 3 4
6
1 6 3 4 5 6
outputCopy
1
3
3
10

"""

# SOLUTION

# correct solution which touches all edge cases
# code is self explanatory
# time complexity is O(n)
# space complexity is O(n)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] - i in d:
            d[a[i] - i] += 1
        else:
            d[a[i] - i] = 1
    count = 0
    for i in d:
        count += (d[i] * (d[i] - 1)) // 2
    print(count)
    