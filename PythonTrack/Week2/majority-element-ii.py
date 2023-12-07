class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        nums_dict={}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num]=1
            else:
                nums_dict[num]+=1
        for key,value in nums_dict.items():
            if value>len(nums)/3:
                ans.append(key)
        return ans

        