import heapq as hq

minHeap=[7,10,6,9,3,15]
hq.heapify(minHeap)

print(hq.heappop(minHeap))


# arr =  [10,20,5,10,5,15]

# prefixSum=[0]*len(arr)
# for i in range(len(arr)):
#     prefixSum[i]=prefixSum[i-1]+arr[i]
# print(prefixSum)
# r=3
# l=1
# print(prefixSum[r]-prefixSum[l])


