"""

C. Longest Strike
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Given an array a
 of length n
 and an integer k
, you are tasked to find any two numbers l
 and r
 (l≤r
) such that:

For each x
 (l≤x≤r)
, x
 appears in a
 at least k
 times (i.e. k
 or more array elements are equal to x
).
The value r−l
 is maximized.
If no numbers satisfy the conditions, output -1.

For example, if a=[11,11,12,13,13,14,14]
 and k=2
, then:

for l=12
, r=14
 the first condition fails because 12
 does not appear at least k=2
 times.
for l=13
, r=14
 the first condition holds, because 13
 occurs at least k=2
 times in a
 and 14
 occurs at least k=2
 times in a
.
for l=11
, r=11
 the first condition holds, because 11
 occurs at least k=2
 times in a
.
A pair of l
 and r
 for which the first condition holds and r−l
 is maximal is l=13
, r=14
.

Input
The first line of the input contains a single integer t
 (1≤t≤1000
) — the number of test cases. The description of test cases follows.

The first line of each test case contains the integers n
 and k
 (1≤n≤2⋅105
, 1≤k≤n
) — the length of the array a
 and the minimum amount of times each number in the range [l,r]
 should appear respectively.

Then a single line follows, containing n
 integers describing the array a
 (1≤ai≤109
).

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.

Output
For each test case output 2
 numbers, l
 and r
 that satisfy the conditions, or "-1" if no numbers satisfy the conditions.

If multiple answers exist, you can output any.

Example
inputCopy
4
7 2
11 11 12 13 13 14 14
5 1
6 3 5 2 1
6 4
4 3 4 3 3 4
14 2
1 1 2 2 2 3 3 3 3 4 4 4 4 4
outputCopy
13 14
1 3
-1
1 4

    """

import sys
from collections import Counter
from collections import defaultdict
from collections import deque
from itertools import accumulate
from itertools import permutations
from itertools import combinations

def input():
    return sys.stdin.readline().strip()

def solve(n, k, a):

    if k == 1:
        return 1, 1

    c = Counter(a)
    if c.most_common(1)[0][1] < k:
        return -1, -1

    l = 0
    r = 0
    for i in range(n):
        if c[a[i]] >= k:
            l = i
            break

    for i in range(n-1, -1, -1):
        if c[a[i]] >= k:
            r = i
            break

    return l+1, r+1

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        l, r = solve(n, k, a)
        print(l, r)