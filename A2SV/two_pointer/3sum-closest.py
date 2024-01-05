class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Lets sort the array first to save space 
        n=len(nums)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if nums[j]<nums[min_index]:
                    min_index=j
            nums[min_index],nums[i]=nums[i],nums[min_index]
        
        closestSum = float('inf')

        for i in range(n):
            left = i + 1
            right = n - 1
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if abs(curr_sum - target) < abs(closestSum - target):
                    closestSum = curr_sum
                
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
        return closestSum
