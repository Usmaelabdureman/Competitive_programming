n = int(input())
a = []
for i in range(n):
    a.append(input())
a.sort(key=len)
for i in range(n):
    for j in range(i + 1, n):
        if a[i] not in a[j]:
            print("NO")
            exit()
print("YES")

for char in a:
    print(char)