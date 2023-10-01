""""
 ABBC or BACB
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given a string s
 made up of characters A
 and B
. Initially you have no coins. You can perform two types of operations:

Pick a substring†
 AB
, change it to BC
, and get a coin.
Pick a substring†
 BA
, change it to CB
, and get a coin.
What is the most number of coins you can obtain?
†
 A substring of length 2
 is a sequence of two adjacent characters of a string.

Input
The input consists of multiple test cases. The first line of the input contains a single integer t
 (1≤t≤1000
) — the number of test cases.

The only line of each test case contains the string s
 (1≤|s|≤2⋅105
). All characters of s
 are either A
 or B
.

The sum of the lengths of s
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output a single integer — the maximum number of coins you can obtain.

Example
inputCopy
8
ABBA
ABA
BAABA
ABB
AAAAAAB
BABA
B
AAA
outputCopy
2
1
3
1
6
2
0
0
Note
In the first test case you can perform the following operations to get 2
 coins:
ABBA→BCBA→BCCB
In the second test case you can perform the following operation to get 1
 coin:
ABA→BCA
In the third test case you can perform the following operations to get 3
 coins:
BAABA→CBABA→CBACB→CCBCB

"""

# SOLUTION

# correct solution which touches all edge cases
# code is self explanatory
# time complexity is O(n)
# space complexity is O(1)




for _ in range(int(input())):
    s = input()
    a = 0
    b = 0
    for i in s:
        if i == 'A':
            a += 1
        else:
            if a > 0:
                a -= 1
            else:
                b += 1
    print(len(s) - (a + b) // 2 * 2)