class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d: 
                d[num] += 1
            else: d[num] = 1
        heap = [(-v, k) for k, v in d.items()]
        heapq.heapify(heap)

        
        res = []
        for i in range(k):
            v, k = heapq.heappop(heap)
            res.append(k)
        return res
