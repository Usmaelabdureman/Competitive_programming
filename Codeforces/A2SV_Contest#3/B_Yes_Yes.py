t = int(input())
for _ in range(t):
    s = input()
    # check if given string s is a substring of  YesYesYes
    yesyes="YesYes"*len(s)
    if s in yesyes:
        print('YES')
    else:
        print('NO')