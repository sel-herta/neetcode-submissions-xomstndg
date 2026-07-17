class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for ui, vi, ti in times:
            adj_list[ui].append([vi, ti])
        min_q = [[0, k]]
        seen = set()
        while min_q:
            c_cost, u = heapq.heappop(min_q)
            if u in seen:
                continue
            seen.add(u)
            if len(seen) == n:
                return c_cost
            for v, t in adj_list[u]:
                if v not in seen:
                    heapq.heappush(min_q, [c_cost + t, v])
        return -1
