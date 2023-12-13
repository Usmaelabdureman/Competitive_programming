class Solution:
    def findLucky(self, arr: List[int]) -> int:
        frequency = {}

        # Count the frequency of each number in the array
        for num in arr:
            frequency[num] = frequency.get(num, 0) + 1

        lucky_number = -1
        # Check for lucky numbers and find the largest among them
        for num, freq in frequency.items():
            if num == freq:
                lucky_number = max(lucky_number, num)

        return lucky_number