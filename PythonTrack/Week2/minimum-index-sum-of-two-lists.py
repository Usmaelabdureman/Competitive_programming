# class Solution:
#     def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = defaultdict(int)
        for i, word in enumerate(list1):
            index_map[word] = i
        res = []
        min_sum = float('inf')
        for j in range(len(list2)):
            if list2[j] in index_map:
                sum_val = j + index_map[list2[j]]
                if sum_val < min_sum:
                    res = [list2[j]]
                    min_sum = sum_val
                elif sum_val == min_sum:
                    res.append(list2[j])
        
        return res
