class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        ans = []
        while nums:
            num = heapq.heappop(nums)
            ans.append(num)
        return ans