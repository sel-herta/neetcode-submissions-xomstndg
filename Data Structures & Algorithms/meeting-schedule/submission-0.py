"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        meetings = []
        for i in range(len(intervals)):
            curStart, curEnd = intervals[i].start, intervals[i].end
            if meetings and meetings[-1].end > curStart:
                return False
            else:
                meetings.append(intervals[i])
        return True