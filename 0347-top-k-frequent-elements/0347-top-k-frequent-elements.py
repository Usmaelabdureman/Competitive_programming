class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # n = len(nums)
        # nums_dict=defaultdict(int)
        # for num in nums:
        #     nums_dict[num]+=1
        # res=sorted(nums_dict.items(),key=lambda value:value[1],reverse=True)
        # print(res)
        # print([res[i][1] for i in range(k)])
        # return [res[i][0] for i in range(k)]

        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq.items():
            buckets[freq].append(num)

        res = []
        for bucket in reversed(buckets):
            if bucket:
                res.extend(bucket)
                if len(res) >= k:
                    break

        return res[:k]
