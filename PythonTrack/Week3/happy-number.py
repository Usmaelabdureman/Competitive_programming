class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 :
            return True
        if n < 6:
            return False
        sumx = 0
        for i in str(n):
            sumx = sumx + int(i)*int(i)
        return self.isHappy(sumx)
                
            


