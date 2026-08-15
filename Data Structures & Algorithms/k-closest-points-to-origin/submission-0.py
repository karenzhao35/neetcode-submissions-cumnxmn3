class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (math.sqrt((x)**2 + (y)**2), [x,y]))
        result = []
        for _ in range(k):
            val, point = heapq.heappop(heap)
            result.append(point)
        return result