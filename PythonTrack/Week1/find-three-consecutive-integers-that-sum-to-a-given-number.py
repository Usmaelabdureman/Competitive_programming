class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x=int(num/3)
        return [x-1,x,x+1] if sum([x-1,x,x+1])==num else []
        