class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)

        # low = 0
        # high = n - 1

        # while high - low >= 0:

            # if nums[low]  == target and nums[high] == target:
            #     return [low,high]
            # elif nums[low] < target :
            #     low += 1
            # else:
            #     high -= 1
            

        n = len(nums)
        low = 0
        high = n - 1

        left = -1

        while low <= high:

            mid = low + (high - low)//2

            if nums[mid] == target:
                left = mid
                high = mid - 1

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        low = 0
        high = n - 1

        right = -1

        while low <= high:

            mid = low + (high - low)//2

            if nums[mid] == target:
                right = mid
                low = mid + 1

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return [left,right]