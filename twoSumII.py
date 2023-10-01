def twoSum(numbers, target):
        lft=0
        rgt=len(numbers)-1
        while lft<rgt:
            res=numbers[lft]+numbers[rgt]
            if res<target:
                lft+=1
            elif res>target:
                rgt-=1
            else:
                return [lft,rgt]
numbers = [1,2,4,7,11,15]
nums=[3,2,4]
target = 6

print(twoSum(nums,target))