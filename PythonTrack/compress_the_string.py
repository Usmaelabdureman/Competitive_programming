from itertools import groupby

s = input().strip()
result = [(len(list(group)), int(key)) for key, group in groupby(s)]
print(*result)
