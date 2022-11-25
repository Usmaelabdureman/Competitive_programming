def targetIndices(nums, target: int):
    sorted=nums.sort(key=len)
    lst=[]

    for i in range(sorted) :
        if target==sorted[i]:
            lst.append(i)
    return lst

num = [1,2,5,2,3]
target=5
print(targetIndices(num,target))

print(num.sort(reverse=False))