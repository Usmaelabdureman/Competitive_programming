class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr={}
        output=[]
        for i in nums:
            if i in arr:
                arr[i]+=1
            else:
                arr[i]=1
        for value in arr.values():
            if value>=2:
                output.append(value)
        return True if len(output)>0 else False
