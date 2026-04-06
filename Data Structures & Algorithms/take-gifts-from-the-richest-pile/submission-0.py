class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)
        for _ in range(k):
            val = heapq.heappop_max(gifts)
            new_val = floor(sqrt(val))
            heapq.heappush_max(gifts, new_val)
        return sum(gifts)