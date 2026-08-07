class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        if not nums: return
        heapq.heapify(self.heap)

        for _ in range(len(nums)-k):
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:


        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]
