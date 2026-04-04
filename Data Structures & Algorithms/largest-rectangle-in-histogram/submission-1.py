class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        maxArea = 0
        for i, height in enumerate(heights):
            s = None
            while stack and stack[-1][1] > height:
                s = stack.pop()
                area = s[1] * (i - s[0])
                maxArea = max(area, maxArea)
            if s:
                stack.append((s[0], height))
            else:
                stack.append((i, height))
        for i, h in stack:
            area = h * (len(heights) - i)
            maxArea = max(maxArea, area)

        return maxArea

        