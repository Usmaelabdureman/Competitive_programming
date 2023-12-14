class UndergroundSystem:
    def __init__(self):
        self.check_ins={}
        self.check_outs=defaultdict(lambda : [0,0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName,t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation,startTime = self.check_ins.pop(id)
        route = (startStation,stationName)
        self.check_outs[route][0]+=1
        self.check_outs[route][1]+=t- startTime
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        numberOfTrips,totalTime = self.check_outs[(startStation,endStation)]
        return totalTime/numberOfTrips
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
