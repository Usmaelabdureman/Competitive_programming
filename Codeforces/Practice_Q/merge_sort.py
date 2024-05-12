from typing import List

def merge(arr: List[int], left: int, mid: int, right: int) -> None:
    left_half = arr[left:mid+1]
    right_half = arr[mid+1:right+1]
    
    i = j = 0
    k = left
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1


def mergeSort(arr: List[int], left: int, right: int) -> None:
    if left < right:
        mid = (left + right) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def test():
    arr = [3, 0, 2, -5, 10, 2]
    mergeSort(arr, 0, len(arr) - 1)
    assert arr == [-5, 0, 2, 2, 3, 10], "Not implemented properly"

    arr = [1, 2, 3]
    mergeSort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3], "Not implemented properly"

    arr = [3, 2, 1]
    mergeSort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3], "Not implemented properly"

    print("Great job!")

test()
