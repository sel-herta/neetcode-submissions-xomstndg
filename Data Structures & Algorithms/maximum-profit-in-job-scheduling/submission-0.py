class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        combined = []
        for i in range(len(startTime)):
            combined.append((startTime[i], endTime[i], profit[i]))
        combined.sort()
        
        memo = {}
        def dfs(i):
            if i >= len(combined):
                return 0
            if i in memo:
                return memo[i]
            res = 0
            skip = dfs(i + 1)
            j = i + 1
            l, r = j, len(combined) - 1
            tryNext = len(combined)
            while l <= r:
                m = (l + r) // 2
                if combined[m][0] >= combined[i][1]:
                    r = m - 1
                    tryNext = m
                else:
                    l = m + 1
            take = combined[i][2] + dfs(tryNext)
            res = max(skip, take)
            memo[i] = res
            return res
        return dfs(0)
