def quick_sort(nums, left, right):
    if left >= right:
        return
    
    pivot_index = partition(nums, left, right)
    quick_sort(nums, left, pivot_index - 1)
    quick_sort(nums, pivot_index + 1, right)

def partition(nums, left, right) -> int:
    # Picks a pivot index and returns the index of pivot value in the sorted array
    
    # write your code here
    pivot_val = nums[left]
    pivot_index = left + 1
    for i in range(left + 1, right + 1):
        if nums[i] < pivot_val:
            nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
            pivot_index += 1
    nums[pivot_index - 1], nums[left] = nums[left], nums[pivot_index - 1]
    
    return pivot_index - 1
    
    
def test():
    arr1 = [3, 0, 2, -5, 10, 2]
    quick_sort(arr1, 0, 5)
    assert arr1 == [-5, 0, 2, 2, 3, 10], "Not Implemented Properly"

    arr2 = [1, 2, 3]
    quick_sort(arr2, 0, 2)
    assert arr2 == [1, 2, 3], "Not Implemented Properly"

    arr3 = [3, 2, 1]
    quick_sort(arr3, 0, 2)
    assert arr3 == [1, 2, 3], "Not Implemented Properly"

    arr4 = [4, 2, 6, 8, 1, 5, 9]
    quick_sort(arr4, 0, 6)
    assert arr4 == [1, 2, 4, 5, 6, 8, 9], "Not Implemented Properly"

    print("Great Job !!!")
test()