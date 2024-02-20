class Solution:
    def fib(self, n: int) -> int:
        if n == 1 : return 1
        if n == 0 : return 0
        return self.fib(n-1) + self.fib(n-2)
        
        # if n < 2:
        #     return n
        # a,b = 0,1
        # for i in range(n-1):
        #     a,b = b,a+b
        # return b
        