class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #sort nums
        nums.sort()
        #Initialize two index variables l as 0 and r as len(nums)-1 to find the candidate elements in the sorted array.
        cnt=0
        l,r=0,len(nums)-1
        while l<r:
            if (nums[l]+nums[r])<k:
                l+=1
            
            elif  nums[l]+nums[r]>k:
                r-=1
            else:
                r-=1
                l+=1
                cnt+=1
        return cnt