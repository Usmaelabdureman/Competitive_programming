from collections import defaultdict

class FrequencyTracker:
    def __init__(self):
        self.freq = defaultdict(int)
        self.freq_count = defaultdict(set)

    def add(self, number: int) -> None:
        prev_freq = self.freq[number]
        self.freq[number] += 1
        if prev_freq in self.freq_count:
            self.freq_count[prev_freq].discard(number)
        self.freq_count[self.freq[number]].add(number)

    def deleteOne(self, number: int) -> None:
        if number in self.freq and self.freq[number] > 0:
            prev_freq = self.freq[number]
            self.freq[number] -= 1
            self.freq_count[prev_freq].discard(number)
            if self.freq[number] > 0:
                self.freq_count[self.freq[number]].add(number)

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq_count and len(self.freq_count[frequency]) > 0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)