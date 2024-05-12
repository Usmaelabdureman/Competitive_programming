"""
. StORage room
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
In Cyprus, the weather is pretty hot. Thus, Theofanis saw this as an opportunity to create an ice cream company.

He keeps the ice cream safe from other ice cream producers by locking it inside big storage rooms. However, he forgot the password. Luckily, the lock has a special feature for forgetful people!

It gives you a table M
 with n
 rows and n
 columns of non-negative integers, and to open the lock, you need to find an array a
 of n
 elements such that:

0≤ai<230
, and
Mi,j=ai|aj
 for all i≠j
, where |
 denotes the bitwise OR operation.
The lock has a bug, and sometimes it gives tables without any solutions. In that case, the ice cream will remain frozen for the rest of eternity.

Can you find an array to open the lock?

Input
The first line contains a single integer t
 (1≤t≤103
) — the number of test cases.

The first line of each test case contains a single integer n
 (1≤n≤103
) — the size of the hidden array.

The next n
 lines describe the rows of M
, line i
 contains the table values Mi,1,Mi,2,…,Mi,n
 (0≤Mi,j<230
).

It is guaranteed that Mi,i=0
 and Mi,j=Mj,i
 for all 1≤i,j≤n
.

It is also guaranteed that the sum of n
 over all test cases does not exceed 103
.

Output
For each test case, if there is a solution print YES and an array that satisfies the property, otherwise print NO.

If there are multiple solutions, print any of them.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Example
inputCopy
4
1
0
4
0 3 3 5
3 0 3 7
3 3 0 7
5 7 7 0
5
0 7 7 5 5
7 0 3 2 6
7 3 0 3 7
5 2 3 0 4
5 6 7 4 0
3
0 0 1
0 0 0
1 0 0
outputCopy
YES
7
YES
1 3 2 5 
YES
5 2 3 0 4
NO

Codeforces (c) Copyright 2010-2023 Mike Mirzayanov

    """
    

# Solution


t = int(input())
for _ in range(t):
    n = int(input())
    M = [list(map(int, input().split())) for _ in range(n)]
    if n == 1:
        print("YES")
        print(0)
    else:
        a = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j:
                    a[i] |= M[i][j]
        print("YES")
        print(*a)