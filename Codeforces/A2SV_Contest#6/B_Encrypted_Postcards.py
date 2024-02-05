"""
Solomon sent Kidus a holiday postcard with a string s
. First, he wrote his greetings with a string a
, consisting of lowercase Latin letters. Solomon wants the greetings to be meaningful for Kidus only so he encrypted according to the following rule into string s
:

after each character of string a
, an arbitrary (possibly zero) number of any lowercase Latin letters, different from the character itself, is added;
after each such addition, the character that he supplemented is added.
Can you help Kidus to understand Solomon's postcard? You are given string s
, and you need to output the initial string a
. In other words, you need to decrypt string s
.

Note that each string encrypted in this way is decrypted uniquely.

Input
The first line of the input contains a single integer t
 (1≤t≤1000
) — the number of test cases.

The descriptions of the test cases follow.

The first line of each test case contains a single integer n
 (2≤n≤100
) — the length of the encrypted message.

The second line of each test case contains a string s
 of length n
 — the encrypted message obtained from some string a
.

Output
For each test case, output the decrypted message a
 on a separate line.

Example
inputCopy
3
8
hbhihbhi
5
ozxco
20
mmeellkkaammbbeeaall
outputCopy
hi
o
melkambeal
inputCopy
2
50
ehjfbsssjkfhenopuoofjkjsjheenkdakuvvuazzaniiqwewdn
30
aiadlakdezzierrefklkkeskseehih
outputCopy
enkuan
adereseh
Note
For the first example: In the first encrypted message, the letter h
 is encrypted as hbh
, and the letter i
 is encrypted as ihbhi
.

In the second encrypted message, only one letter o
 is encrypted as ozxco
.

In the third encrypted message, zero characters are added to each letter.
    """
    
# SOLUTION:
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = ""
    left = 0
    right = 1
    while right < n:
        if s[left] != s[right]:
            right+=1
        else:
            ans += s[left]
            left = right+1
            right=left+1
    print(ans)