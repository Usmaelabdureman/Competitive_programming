class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        # if n<1: return False
        # while(n%4==0):
        #     n=n//4
        # return True if n==1 else False

        if n < 1:
            return False
        elif n == 1:
            return True
        return self.isPowerOfFour(n / 4)
       