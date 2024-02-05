"""
You are given an array a
 consisting of n
 integers numbered from 1
 to n
.

Let's define the m
-lucky number of the array as the smallest number that occurs in all of the subarrays of the array having length m
 (recall that a subarray of a
 of length m
 is a contiguous part of a
 containing exactly m
 elements). If there is no integer occuring in all subarrays of length m
 for some value of m
, then the m
-lucky number is −1
.

For each m
 from 1
 to n
 calculate the m
-lucky number of the array a
.

Input
The first line contains one integer t
 (1≤t≤1000
) — the number of test cases. Then t
 test cases follow.

The first line of each test case contains one integer n
 (1≤n≤3⋅105
) — the number of elements in the array. The second line contains n
 integers a1,a2,…,an
 (1≤ai≤n
) — the elements of the array.

It is guaranteed that the sum of n
 over all test cases does not exceed 3⋅105
.

Output
For each test case print n
 integers, where the i
-th integer is equal to the i
-lucky number of the array.

Example
inputCopy
3
5
1 2 3 4 5
5
4 4 4 4 2
6
1 3 1 5 3 1
outputCopy
-1 -1 3 2 1 
-1 4 4 4 2 
-1 -1 1 1 1 1 

    """
def generate_subarrays(a, m):
    subarrays = []
    for i in range(len(a) - m + 1):
        subarray = a[i:i + m]
        subarrays.append(subarray)
    return subarrays

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for m in range(1, n + 1):
        subarrays = generate_subarrays(a, m)
        common = set(subarrays[0])
        for subarray in subarrays[1:]:
            common &= set(subarray)
        if common:
            ans.append(min(common))
        else:
            ans.append(-1)
    print(*ans)
