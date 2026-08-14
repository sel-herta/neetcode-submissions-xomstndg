class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for cs, ce in intervals:
            if ans and ans[-1][1] >= cs:
                ans[-1][1] = max(ans[-1][1], ce)
            else:
                ans.append([cs, ce])
        return ans