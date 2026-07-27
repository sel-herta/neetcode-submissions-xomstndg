class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, p in flights:
            adj_list[u].append([v, p])
        dist = [[float('inf')] * (k + 5) for _ in range(n)]
        dist[src][0] = 0
        min_heap = [(0, src, -1)]

        ans = float('inf')
        while min_heap:
            c_cost, u, c_k = heapq.heappop(min_heap)
            if c_k > k:
                continue
            if u == dst:
                ans = min(ans, c_cost)
            for v, p in adj_list[u]:
                if dist[v][c_k] > c_cost + p:
                    dist[v][c_k] = c_cost + p
                    heapq.heappush(min_heap, (c_cost + p, v, c_k + 1))
        return -1 if ans == float('inf') else ans