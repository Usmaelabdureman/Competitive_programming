
def minSubArraySum(nums,target):
    minWindow =float('inf')
    currentSum=0
    left=0
    for right in range(len(nums)):
        currentSum+=nums[right]
        while currentSum>=target:
            minWindow=min(minWindow,right-left+1)
            currentSum-=nums[left]
            left+=1
    return 0 if minWindow ==float('inf') else minWindow

if __name__ == "__main__":
    nums = [1,0,0,1,1,0,1,0,1,1,1]
    target = 5
    print(minSubArraySum(nums,target))
    
    
        
        
        
    
    
    