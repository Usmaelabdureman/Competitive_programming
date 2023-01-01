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
                return [lft+1,rgt+1]

numbers = [1,2,4,7,11,15]
target = 9

print(twoSum(numbers,target))