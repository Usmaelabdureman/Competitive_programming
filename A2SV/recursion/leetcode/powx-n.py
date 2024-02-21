class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recur(x,n):
            if n==0:return 1
            if x==0:return 0
            result=recur(x,n//2)
            result=result*result
            return x*result if n%2!=0 else result
        result=recur(x,abs(n))
        return result if n>=0 else 1/result