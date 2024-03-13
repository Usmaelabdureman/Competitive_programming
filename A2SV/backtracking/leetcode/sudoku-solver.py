class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(num, row, col):
            return (
                str(num) not in rows[row] and
                str(num) not in cols[col] and
                str(num) not in subgrids[3 * (row // 3) + col // 3]
            )

        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in map(str, range(1, 10)):
                            if isValid(num, i, j):
                        
                                board[i][j] = num
                                rows[i].add(num)
                                cols[j].add(num)
                                subgrids[3 * (i // 3) + j // 3].add(num)

                            
                                if backtrack():
                                    return True

                                board[i][j] = '.'
                                rows[i].remove(num)
                                cols[j].remove(num)
                                subgrids[3 * (i // 3) + j // 3].remove(num)

                        return False
            return True

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrids = [set() for _ in range(9)]



        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    subgrids[3 * (i // 3) + j // 3].add(num)

        backtrack()

