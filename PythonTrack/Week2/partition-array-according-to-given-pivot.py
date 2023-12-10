class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than_pivot=[num for num in nums if num<pivot]
        equal_to_pivot =[num for num in nums if num == pivot]
        gt_pivot = [num for num in nums if num>pivot]
        return less_than_pivot + equal_to_pivot + gt_pivot
        