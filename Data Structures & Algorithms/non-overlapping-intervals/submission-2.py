class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort()
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            curStart, curEnd = intervals[i]
            if curStart >= prevEnd:
                prevEnd = curEnd
            else:
                prevEnd = min(prevEnd, curEnd)
                ans += 1
        return ans