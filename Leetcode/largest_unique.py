def largestUniqueNumber(A):
    frequency = {}
    
    for num in A:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    unique_numbers = [num for num, freq in frequency.items() if freq == 1]
    
    if not unique_numbers:
        return -1
    return max(unique_numbers)

# Example usage:
arr1 = [5, 7, 3, 9, 4, 9, 8, 3, 1]
print(largestUniqueNumber(arr1))  # Output: 8

arr2 = [9, 9, 8, 8]
print(largestUniqueNumber(arr2))  # Output: -1
