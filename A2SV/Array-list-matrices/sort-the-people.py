class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

            merged = [[a, b] for a, b in zip(names, heights)]
            for i in range(len(merged)):
                min_index = i
                for j in range(i + 1, len(merged)):
                    if merged[min_index][1] < merged[j][1]:
                        min_index = j
                merged[i], merged[min_index] = merged[min_index], merged[i]
            
            return [name for name ,_ in merged]
 
            