class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        array=[i for i in range(1,n+1)]
        i=0
        for _ in range(n-1):
            l  = len(array)
            i = (i+(k-1))%l
            array.pop(i)
        return array[0]
        