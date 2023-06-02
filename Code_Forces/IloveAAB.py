t = int(input())
for _ in range(t):
    s = input().strip()
    if s[-1] == 'A':
        print('NO')
        continue
    substrings = s.split('B')
    for substring in substrings[:-1]:
        if not substring.startswith('A') or 'B' in substring:
            print('NO')
            break
    else:
        print('YES')
