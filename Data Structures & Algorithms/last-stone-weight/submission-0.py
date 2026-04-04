class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) >= 2:
            x, y = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if x - y > 0:
                heapq.heappush_max(stones, x - y)
        if len(stones) > 0:
            return stones[0]
        else:
            return 0