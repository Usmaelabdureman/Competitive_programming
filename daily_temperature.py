class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr_len = len(temperatures)
        mono_stack = []
        ans = [0] * arr_len
        for i in range(arr_len):
            if (len(mono_stack) > 0 and temperatures[i] > mono_stack[-1][0]):
                while len(mono_stack) > 0 and temperatures[i] > mono_stack[-1][0]:
                    ans[mono_stack[-1][1]] = i - mono_stack[-1][1]
                    mono_stack.pop()
            mono_stack.append((temperatures[i], i))
        return ans 