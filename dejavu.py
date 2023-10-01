t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    if s == s[::-1]:
        print("NO")
    else:
        for i in range(n):
            if s[i] != 'a':
                new_s = s[:i] + 'a' + s[i:]
                if new_s != new_s[::-1]:
                    print("YES")
                    print(new_s)
                    break
        else:
            print("NO")
