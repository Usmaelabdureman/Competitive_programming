
def cycleSort(arr):
    n = len(arr)
    i = 0
    while i < n:
        correct_position = arr[i] - 1
        if correct_position != i:
            arr[correct_position], arr[i] = arr[i], arr[correct_position]
        else:
            i += 1
    return arr

test = [4,3,2,1]
print(cycleSort(test))