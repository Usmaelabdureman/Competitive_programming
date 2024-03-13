class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        # Think it as Binary Tree  where 
        #  First half is invert( bit flip )  of second half.
        #      0
        #    /   \
        #   0     1
        #  / \    / \
        # 0   1  1   0

        # Base case 
        if n == 1 or k == 1:
            return 0  

        if k % 2 == 1: 

            return self.kthGrammar(n-1, (k+1)//2)  

        if k % 2 == 0:  
            return  abs(self.kthGrammar(n-1, k//2)-1)
        