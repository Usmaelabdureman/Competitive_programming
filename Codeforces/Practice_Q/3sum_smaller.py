
def threeSumSmaller(nums,target):
    nums.sort()
    n=len(nums)
    count=0
    for i in range(n):
        left =i+1
        right =n-1
        
        while left < right:
            threeSum=nums[i]+nums[left]+nums[right]
            if threeSum<target and left < right:
                count+=(right-left)
                left+=1
            else: 
                right-=1
    return count
test =[-2,0,1,3]
target =2
print(threeSumSmaller(test,target))
test2=[]
print(threeSumSmaller(test2,target=0))