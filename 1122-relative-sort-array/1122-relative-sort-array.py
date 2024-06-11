class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        index_dict = {num: i for i, num in enumerate(arr2)}
       
        def custom_sort(num):
            return (index_dict[num], num) if num in index_dict else (len(arr2) + num, num)
            
        arr1.sort(key=custom_sort)
        return arr1