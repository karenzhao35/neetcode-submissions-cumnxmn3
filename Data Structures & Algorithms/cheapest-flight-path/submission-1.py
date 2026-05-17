class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = {}
        adj = defaultdict(list)
        for from_i, to_i, price_i in flights: 
            adj[from_i].append(to_i)
            edges[(from_i, to_i)] = price_i
        
        heap = [(0, [src])]
        while heap: 
            price, path = heapq.heappop(heap)
            curr = path[-1]
            if curr == dst: return price
            if len(path) < k+2:
                for v in adj[curr]:
                    heapq.heappush(heap, (price + edges[(curr, v)], path+[v]))

        return -1

