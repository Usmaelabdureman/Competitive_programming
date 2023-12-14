class MyHashMap:

    def __init__(self):
        self.hashT=[-1]*(10**6+1)
        
    def put(self, key: int, value: int) -> None:
        self.hashT[key]=value
        
    def get(self, key: int) -> int:
        return self.hashT[key]
        
    def remove(self, key: int) -> None:
        self.hashT[key]=-1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)