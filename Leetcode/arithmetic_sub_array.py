class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        len_l = len_r = len(l)
        output = []
        result = []
        for i in range(len_l):
            output = nums[l[i]:r[i]+1]
            output.sort()
            diff= output[1] - output[0]
            for i in range(1, len(output)):
                if output[i] - output[i-1] != diff:
                    result.append(False)
                    break
                elif (i == len(output) - 1):
                    result.append(True)
        return result