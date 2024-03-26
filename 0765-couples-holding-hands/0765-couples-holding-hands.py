class Solution:

    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        swaps = 0
    
        for i in range(0, len(row), 2):
            while row[i] // 2 != row[i + 1] // 2:
                partner_index = row.index(row[i] // 2 * 2 + 1 if row[i] % 2 == 0 else row[i] // 2 * 2)
                row[i + 1], row[partner_index] = row[partner_index], row[i + 1]
                swaps += 1
        
        return swaps
