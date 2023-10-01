class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if len(arr)==1:return []

        def flip(sublist, k):
            i = 0
            while i < k / 2:
                sublist[i], sublist[k-i-1] = sublist[k-i-1], sublist[i]
                i += 1
        result = []
        len_arr = len(arr)
        while len_arr > 0:
            # locate the position for the value to sort in this round
            indx=arr.index(len_arr)

            # sink the value_to_sort to the bottom,
            #   with at most two steps of pancake flipping.
            if indx != len_arr - 1:
                # flip the value to the head if necessary
                if indx != 0:
                    result.append(indx+1)
                    flip(arr, indx+1)
                # now that the value is at the head, flip it to the bottom
                result.append(len_arr)
                flip(arr, len_arr)

            # move on to the next round
            len_arr -= 1

        return result