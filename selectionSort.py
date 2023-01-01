#User function Template for python3
class Solution: 
    def select(self, arr, i):
        minIdx = i
        min_elt = arr[i]
        for i in range(i, len(arr)):
            if arr[i] < min_elt:
                min_elt = arr[i]
                minIdx = i
        return minIdx
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            index = self.select(arr, i)
            arr[i], arr[index] = arr[index], arr[i]
        return arr