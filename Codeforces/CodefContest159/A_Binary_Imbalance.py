"""
You are given a string s
, consisting only of characters '0' and/or '1'.

In one operation, you choose a position i
 from 1
 to |s|−1
, where |s|
 is the current length of string s
. Then you insert a character between the i
-th and the (i+1)
-st characters of s
. If si=si+1
, you insert '1'. If si≠si+1
, you insert '0'.

Is it possible to make the number of zeroes in the string strictly greater than the number of ones, using any number of operations (possibly, none)?

Input
The first line contains a single integer t
 (1≤t≤100
) — the number of testcases.

The first line of each testcase contains an integer n
 (1≤n≤100
).

The second line contains a string s
 of length exactly n
, consisting only of characters '0' and/or '1'.

Output
For each testcase, print "YES" if it's possible to make the number of zeroes in s
 strictly greater than the number of ones, using any number of operations (possibly, none). Otherwise, print "NO".

Example
inputCopy
3
2
00
2
11
2
10
outputCopy
YES
NO
YES
Note
In the first testcase, the number of zeroes is already greater than the number of ones.

In the second testcase, it's impossible to insert any zeroes in the string.

In the third testcase, you can choose i=1
 to insert a zero between the 1
-st and the 2
-nd characters. Since s1≠s2
, you insert a '0'. The resulting string is "100". It has two zeroes and only a single one, so the answer is "YES".
    """

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    if s.count('0') > s.count('1'):
        print("YES")
    elif '0' not in s:
        print("NO")
    else:
        print("YES")