class Solution:
    def countPrimes(self, n: int) -> int:
        lst_prime = []
        isPrime = [True]*( n )
        
        for i in range(2,n):
            if isPrime[i] and (i%2==1 or i==2):
                lst_prime.append(i)
                # eliminate the multiple of 2
                for j in range(i*i,n,i):
                    isPrime[j] = False
                    
        return len(lst_prime)