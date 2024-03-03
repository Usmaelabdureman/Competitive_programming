class Solution:
    
    def isValid(self,row,col,path):
        for prev_row, prev_corr in enumerate(path):
                prev_col = prev_corr.index('Q')
                if prev_col == col or prev_row - prev_col == row - col or prev_row + prev_col == row + col:
                    return False
        return True
        
    def totalNQueens(self, n: int) -> int:

        def backtrack(row=0, path=[]):
            #  Base Case
            if row == n:
                res.append(path[:])
                return

                # Candidates

            for col in range(n):
                if self.isValid(row, col, path):
                    path.append("." * col + "Q" + "." * (n - col - 1))
                    backtrack(row + 1, path)
                    path.pop()
        res = []
        backtrack()
        return len(res)
