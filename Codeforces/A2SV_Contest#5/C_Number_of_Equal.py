n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

count = 0
list1_pointer = 0
list2_pointer = 0
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            count+=1
print(count)