class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [str(x) for x in nums]
        if len(set(arr)) == 1 and arr[0] == '0':
            return '0'
        def comparator(x,y):

            if x+y>y+x:
               return 1
            
            else:
                return -1
        ans=sorted(arr,key=cmp_to_key(comparator),reverse=True)
        return ''.join(ans)