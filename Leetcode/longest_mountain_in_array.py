class Solution:
    def longestMountain(self, arr):
        len_arr= len(arr)
        result = 0
        base = 0
        while base < len_arr:
            end = base
            #if base is a left-boundary
            if end + 1<len_arr and arr[end]<arr[end + 1]:
                #set end to the peak of this potential mountain
                while end+1 < len_arr and arr[end] < arr[end+1]:
                    end += 1
                if end + 1 < len_arr and arr[end] > arr[end + 1]: #if end is really a peak..
                    #set 'end' to right-boundary of mountain
                    while end+1 < len_arr and arr[end] > arr[end+1]:
                        end += 1
                    #record candidate answer
                    result = max(result, end - base + 1)
            base = max(end, base + 1)
        return result
        