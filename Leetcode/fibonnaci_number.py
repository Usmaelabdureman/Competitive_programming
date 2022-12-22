class Solution:
    def fib(self, n: int) -> int:
        first=0
        second=1
        res=0
        if n<=1:return n
        for i in range(2,n+1):
            temp=first+second
            first=second
            second=temp
            res=temp
        return  res