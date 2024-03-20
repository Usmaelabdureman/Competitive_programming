class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergeSort(arr, result):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = mergeSort(arr[:mid], result)
            right = mergeSort(arr[mid:], result)
            merged = []
            left_index = right_index = 0
            
            while left_index < len(left) and right_index < len(right):
                if left[left_index][1] <= right[right_index][1]:
                    merged.append(left[left_index])
                    result[left[left_index][0]] += right_index
                    left_index += 1
                else:
                    merged.append(right[right_index])
                    right_index += 1
            
            while left_index < len(left):
                merged.append(left[left_index])
                result[left[left_index][0]] += right_index
                left_index += 1
            
            while right_index < len(right):
                merged.append(right[right_index])
                right_index += 1
            
            return merged
        
        res = [0] * len(nums)
        indxd_nums = [(i, num) for i, num in enumerate(nums)]
        mergeSort(indxd_nums, res)
        return res
