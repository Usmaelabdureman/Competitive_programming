class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left=0
        right=n
        newArray=[]
        while left < n and right < len(nums):
            newArray.append(nums[left])
            newArray.append(nums[right])
            left+=1
            right+=1
        return newArray


