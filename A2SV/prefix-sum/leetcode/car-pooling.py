class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = max(trips[i][2] for i in range(len(trips)))
        arr = [0] * (n+1)

        for trip in trips:
            num_pass,_from,to = trip
            arr[_from] += num_pass
            arr[to] -= num_pass
            
        max_sum = 0
        curr_sum = 0
        for num in arr:
            curr_sum += num
            max_sum = max(curr_sum,max_sum)
        return capacity >= max_sum
