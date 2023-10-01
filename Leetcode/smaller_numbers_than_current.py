def test(arr):
    sorted_arr=arr.sort()
    myDict={}
    res=[]
    for i in range(len(sorted_arr)):
        if sorted_arr[i] not in myDict:
            myDict[sorted_arr[i]]=i
    for i in arr:
        if i in myDict:
            res.append(myDict[i])
    return res



ls=[8,1,2,2,3]
print(test(ls))