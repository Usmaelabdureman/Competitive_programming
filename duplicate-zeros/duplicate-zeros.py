class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new_arr = [0] * (len(arr)+arr.count(0))  # Create a new array of the same length initialized with zeros
        
        j = 0  # Index for the new array
        
        for i in range(len(arr)):
            if arr[i] == 0:
                # Duplicate zero
                new_arr[j] = 0
                j += 1
            else:
                # Copy non-zero elements
                new_arr[j] = arr[i]
            j += 1
        for i in range(len(arr)):
            arr[i]=new_arr[i]