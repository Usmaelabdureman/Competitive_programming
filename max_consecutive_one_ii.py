def findMaxConsecutiveOnes(arr):
    maxOneCount,l=0,0
    while l<len(arr):
        if arr[l]==0:
            l+=1
        else:
            r=l
            while r<len(arr)-1 and arr[r+1]==1:
                r+=1
            maxOneCount=max(maxOneCount,r-l+1)
            l=r+1
                
    return maxOneCount
#using two loop with O(n^2) looks the following
# def findMaxconsOnes(arr):
#     maxOneCount=0
#     for i in range(len(arr)):
#         maxCount=0
#         for j in range(i,len(arr)):
#                 if arr[j]==1:
#                     maxCount+=1
#                 else:
#                     break
#                 maxOneCount=max(maxOneCount,maxCount)
#     return maxOneCount
ts=[0,1,1,1,1,0,0,1,1]
print(findMaxConsecutiveOnes(ts))