import sys
sys.set_int_max_str_digits(1<<20)

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def recur(x,n):
            if n==0:return 1
            if x==0:return 0
            
            result=recur(x,n//2)
            result%=MOD
            result =result*result 
            return x*result if n%2!=0 else result

        half = n//2

        five = recur(5,half)
        four = recur(4,half)

        four = four % MOD
    
        five = five % MOD
        
        result = (five * four * 5) if n%2 != 0 else five * four
 
        return result % MOD