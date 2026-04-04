class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            ans = max(area, ans)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ans
            