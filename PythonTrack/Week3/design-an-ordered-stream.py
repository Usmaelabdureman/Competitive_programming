class OrderedStream:

    def __init__(self, n: int):
        self.input=[None]*n
        self.pointer=0
        #
    def insert(self, idKey: int, value: str) -> List[str]:
        self.input[idKey-1]=value
        result=[]
        while self.pointer < len(self.input) and self.input[self.pointer]:
            result.append(self.input[self.pointer])
            self.pointer+=1
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)