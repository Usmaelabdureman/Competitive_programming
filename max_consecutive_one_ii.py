#by using sliding window technique 
#time complexity O(n)
#space complexity O(1)
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