class Solution:
    def duplicateZeroes(self, arr):
        new_arr = [0]*(len(arr)+arr.count(0))
        j = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                new_arr[j] = 0
                j += 1
            new_arr[j] = arr[i]
            j += 1
        for i in range(len(arr)):
            arr[i] = new_arr[i]
            
test = [1, 0, 2, 3, 0, 4, 5, 0]
t = Solution()
t.duplicateZeroes(test)
print(test)
