import random

class RandomizedSet:
    def __init__(self):
        self.data = []  # Array list to store values
        self.val_to_index = {}  # Hashmap to store value -> its index

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False

        self.data.append(val)
        self.val_to_index[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        # Swap the value to delete with the last element
        index = self.val_to_index[val]
        last_val = self.data[-1]
        self.data[index] = last_val
        self.val_to_index[last_val] = index

        # Remove the last element
        self.data.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()