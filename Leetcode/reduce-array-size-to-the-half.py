class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        count_sorted = list(count.values())
        count_sorted.sort(reverse=True)
        res = 0
        for number in range(len(count_sorted)):
            res += count_sorted[number]
            if res >= (len(arr)//2):
                return number + 1