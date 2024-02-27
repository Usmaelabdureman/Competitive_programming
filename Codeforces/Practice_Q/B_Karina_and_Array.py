
"""
Karina has an array of n
 integers a1,a2,a3,…,an
. She loves multiplying numbers, so she decided that the beauty of a pair of numbers is their product. And the beauty of an array is the maximum beauty of a pair of adjacent elements in the array.

For example, for n=4
, a=[3,5,7,4]
, the beauty of the array is max
(3⋅5
, 5⋅7
, 7⋅4
) = max
(15
, 35
, 28
) = 35
.

Karina wants her array to be as beautiful as possible. In order to achieve her goal, she can remove some elements (possibly zero) from the array. After Karina removes all elements she wants to, the array must contain at least two elements.

Unfortunately, Karina doesn't have enough time to do all her tasks, so she asks you to calculate the maximum beauty of the array that she can get by removing any number of elements (possibly zero).

Input
The first line of the input contains an integer t
 (1≤t≤104
) — the number of test cases.

The description of the test cases follows.

The first line of a test case contains an integer n
 (2≤n≤2⋅105
) — the length of the array a
.

The second line of a test case contains n
 integers a1,a2,a3,…,an
 (−109≤ai≤109
) — the elements of the array a
.

The sum of all values of n
 across all test cases does not exceed 2⋅105
.

Output
Output t
 integers, each of which is the answer to the corresponding test case — the maximum beauty of the array that Karina can get.

Example
inputCopy
7
4
5 0 2 1
3
-1 1 0
5
2 0 -1 -4 0
6
-8 4 3 7 1 -9
6
0 3 -2 5 -4 -4
2
1000000000 910000000
7
-1 -7 -2 -5 -4 -6 -3
outputCopy
10
0
4
72
16
910000000000000000
42
Note
In the first test case of the example, to get the maximum beauty, you need to remove the 2
-nd element.

In the second and third test cases of the example, there is no need to remove any elements to achieve maximum beauty.

In the fourth test case of the example, you need to leave only the first and last elements.
    """
    

# Solution:

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    max_beauty = max(a[-1]*a[-2], a[0]*a[1])
    print(max_beauty)