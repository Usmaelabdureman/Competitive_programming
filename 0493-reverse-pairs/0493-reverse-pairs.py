class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count=0
        def compare(arr1,arr2):
            nonlocal count
            p1,p2=0,0
            print("here")
            while p1<len(arr1) and p2<len(arr2):
                if arr1[p1]>(2*arr2[p2]):
                    count+=(len(arr1)-p1)
                    p2+=1
                else:
                    p1+=1
        def merge(left_half,right_half) -> List[int]:
            merged = []
            l1, l2 = 0, 0
            r1, r2 = len(left_half), len(right_half)
            
            while l1 < r1 and l2 < r2:
                if left_half[l1] <= right_half[l2]:
                    merged.append(left_half[l1])
                    l1 += 1
                else:
                    merged.append(right_half[l2])
                    l2 += 1
            
            while l1 < r1:
                merged.append(left_half[l1])
                l1 += 1
            
            while l2 < r2:
                merged.append(right_half[l2])
                l2 += 1
            
            return merged


        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2

            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
            compare(left_half,right_half)
            return merge(left_half, right_half)
        mergeSort(0,len(nums)-1,nums)
        return count