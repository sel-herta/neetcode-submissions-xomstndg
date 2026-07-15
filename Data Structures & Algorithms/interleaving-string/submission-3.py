class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def dfs(i, j, k):
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            state = (i, j)
            if state in memo:
                return memo[state]
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = dfs(i + 1, j, k + 1)
            if not res and j < len(s2) and s2[j] == s3[k]:
                res = dfs(i, j + 1, k + 1)
            memo[state] = res
            return res
        return dfs(0, 0, 0)