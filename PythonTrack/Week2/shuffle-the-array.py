class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        pointer1=0
        pointer2=int(len(nums)/2)
        while pointer1<len(nums)/2:
            ans.extend([nums[pointer1],nums[pointer2]])
            pointer1+=1
            pointer2+=1
        return ans

        