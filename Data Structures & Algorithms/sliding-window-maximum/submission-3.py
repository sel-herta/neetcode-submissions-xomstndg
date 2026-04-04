class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque() # stores (index, val)
        l = 0
        if k > len(nums):
            return ans
        for r, num in enumerate(nums):
            while queue and nums[r] > queue[-1][1]:
                queue.pop()
            queue.append((r, num))
            if r + 1 >= k:
                ans.append(queue[0][1])
                if queue[0][0] < l + 1:
                    queue.popleft()
                l += 1
        return ans