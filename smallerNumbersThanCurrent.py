def smallerNumbersThanCurrent(nums):
        l1 = sorted(nums)
        return [l1.index(i) for i in nums]

lst=[8,1,2,3,2,4]

print(smallerNumbersThanCurrent(lst))


def small(n):
    lst={}

    cnt=0
    for i in n:
        if i in lst and i<lst.keys:
            lst[i]+=1
        else:
            lst[i]=0
    return lst.values

print(small(lst))
