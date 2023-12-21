class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deleted_col=0
        for col in range(len(strs[0])):
            for row in range(1,len(strs)):
                if strs[row][col] < strs[row - 1][col]:
                    deleted_col+=1
                    break
        return deleted_col

        