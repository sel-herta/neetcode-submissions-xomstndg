class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        ans = []
        # the intervals are already sorted and nonoverlapping
        # first check if the newInterval comes before the first interval

        if newInterval[1] < intervals[0][0]:
            ans.append(newInterval)
            return ans + intervals
        
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        ans.append(newInterval)
        while i < n:
            ans.append(intervals[i])
            i += 1
        return ans

            