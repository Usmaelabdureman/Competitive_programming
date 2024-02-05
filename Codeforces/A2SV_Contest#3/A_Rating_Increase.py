"""
Rating Increase
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Monocarp is a great solver of adhoc problems. Recently, he participated in an Educational Codeforces Round, and gained rating!

Monocarp knew that, before the round, his rating was a
. After the round, it increased to b
 (b>a
). He wrote both values one after another to not forget them.

However, he wrote them so close to each other, that he can't tell now where the first value ends and the second value starts.

Please, help him find some values a
 and b
 such that:

neither of them has a leading zero;
both of them are strictly greater than 0
;
b>a
;
they produce the given value ab
 when written one after another.
If there are multiple answers, you can print any of them.

Input
The first line contains a single integer t
 (1≤t≤104
) — the number of testcases.

The only line of each testcase consists of a single string ab
 of length from 2
 to 8
 that:

consists only of digits;
doesn't start with a zero.
Output
For each testcase, determine if such values a
 and b
 exist. If they don't, print -1. Otherwise, print two integers a
 and b
.

If there are multiple answers, you can print any of them.

Example
inputCopy
5
20002001
391125
200200
2001000
12
outputCopy
2000 2001
39 1125
-1
200 1000
1 2
Note
In the second testcase, printing 3
 and 91125
 is also valid.

In the third testcase, 20
 and 0200
 is not valid, because b
 has a leading zero. 200
 and 200
 is not valid, because 200
 is not strictly greater than 200
.

    """
    
# Solution:

t = int(input().strip())
for _ in range(t):
    # Example Input Parsing
    testcases =input().split()

    for ab in testcases:
        n = len(ab)
        found = False

        # Try all possible lengths for 'a'
        for i in range(1, n):
            a_str = ab[:i]
            a = int(a_str)

            # If 'a' has leading zeros or is zero, skip
            if a_str != str(a) or a == 0:
                continue

            # Find 'b' from the remaining part of the string
            b_str = ab[i:]
            b = int(b_str)

            # If 'b' has leading zeros or is zero, skip
            if b_str != str(b) or b == 0:
                continue

            # If 'b' is strictly greater than 'a', print the values and break
            if b > a:
                print(a, b)
                found = True
                break
        
        # If no valid values found for the current testcase, print -1
        if not found:
            print(-1)
