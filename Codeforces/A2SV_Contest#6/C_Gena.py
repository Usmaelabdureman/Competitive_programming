n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
b = sorted(map(int, input().split()))

astu_pointer = 0
aait_pointer = 0
ans = 0
while astu_pointer < n and aait_pointer < m:
    if abs(a[astu_pointer] - b[aait_pointer]) <= 1:
        ans += 1
        astu_pointer += 1
        aait_pointer += 1
    elif a[astu_pointer] < b[aait_pointer]:
        astu_pointer += 1
    else:
        aait_pointer += 1
print(ans)