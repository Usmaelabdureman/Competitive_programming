"""
B. Divisibility by 2^n
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given an array of positive integers a1,a2,…,an
.

Make the product of all the numbers in the array (that is, a1⋅a2⋅…⋅an
) divisible by 2n
.

You can perform the following operation as many times as you like:

select an arbitrary index i
 (1≤i≤n
) and replace the value ai
 with ai=ai⋅i
.
You cannot apply the operation repeatedly to a single index. In other words, all selected values of i
 must be different.

Find the smallest number of operations you need to perform to make the product of all the elements in the array divisible by 2n
. Note that such a set of operations does not always exist.

Input
The first line of the input contains a single integer t
 (1≤t≤104
) — the number test cases.

Then the descriptions of the input data sets follow.

The first line of each test case contains a single integer n
 (1≤n≤2⋅105
) — the length of array a
.

The second line of each test case contains exactly n
 integers: a1,a2,…,an
 (1≤ai≤109
).

It is guaranteed that the sum of n
 values over all test cases in a test does not exceed 2⋅105
.

Output
For each test case, print the least number of operations to make the product of all numbers in the array divisible by 2n
. If the answer does not exist, print -1.

Example
inputCopy
6
1
2
2
3 2
3
10 6 11
4
13 17 1 1
5
1 1 12 1 1
6
20 7 14 18 3 5
outputCopy
0
1
1
-1
2
1
Note
In the first test case, the product of all elements is initially 2
, so no operations needed.

In the second test case, the product of elements initially equals 6
. We can apply the operation for i=2
, and then a2
 becomes 2⋅2=4
, and the product of numbers becomes 3⋅4=12
, and this product of numbers is divided by 2n=22=4
.

In the fourth test case, even if we apply all possible operations, we still cannot make the product of numbers divisible by 2n
  — it will be (13⋅1)⋅(17⋅2)⋅(1⋅3)⋅(1⋅4)=5304
, which does not divide by 2n=24=16
.

In the fifth test case, we can apply operations for i=2
 and i=4
.

"""
#





 

 