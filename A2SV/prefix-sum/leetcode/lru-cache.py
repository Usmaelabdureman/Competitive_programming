

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.remain = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key) 
        return self.cache.get(key)

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.cache.popitem(last=False) 
        else:
            self.cache.pop(key)
        self.cache[key] = value 