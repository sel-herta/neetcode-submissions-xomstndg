class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        while k > 0:
            k -= 1
            val = heapq.heappop_max(nums)
            if k == 0:
                return val